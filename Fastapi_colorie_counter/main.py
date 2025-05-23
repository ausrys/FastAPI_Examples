from enum import Enum

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()


class TrainingType(str, Enum):
    walking = "walking"
    running = "running"
    crossfit = "crossfit"


class TrainingInput(BaseModel):
    type: TrainingType
    amount: float  # km for walking/running, number of exercises for crossfit


class CalorieCalculator:
    __slots__ = ('weight',)

    def __init__(self, weight: float = 70.0):
        self.weight = weight  # in kilograms

    @staticmethod
    def calculate_walking(km: float, weight: float) -> float:
        return km * 0.5 * weight

    @staticmethod
    def calculate_running(km: float, weight: float) -> float:
        return km * 0.9 * weight

    @staticmethod
    def calculate_crossfit(exercises: float, weight: float) -> float:
        return exercises * 5 * weight

    def calculate(self, t_type: TrainingType, amount: float) -> float:
        if t_type == TrainingType.walking:
            return self.calculate_walking(amount, self.weight)
        elif t_type == TrainingType.running:
            return self.calculate_running(amount, self.weight)
        elif t_type == TrainingType.crossfit:
            return self.calculate_crossfit(amount, self.weight)
        else:
            raise ValueError("Invalid training type")


@app.post("/calculate_calories")
def calculate_calories(training: TrainingInput):
    if training.amount <= 0:
        raise HTTPException(status_code=400, detail="Amount must be positive")

    calculator = CalorieCalculator()
    calories = calculator.calculate(training.type, training.amount)
    return {"calories_burned": round(calories, 2)}
