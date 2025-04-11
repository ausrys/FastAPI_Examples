class AppException(Exception):
    def __init__(self, status_code: int, description: str, solve: str):
        self.status_code = status_code
        self.description = description
        self.solve = solve
