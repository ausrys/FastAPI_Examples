from fastapi import FastAPI
import sports
from database import Base, engine
import uvicorn

app = FastAPI(title="Sports Scraper API")

# Include router
app.include_router(sports.router)

if __name__ == "__main__":
    uvicorn.run("app.main:app", host="0.0.0.0", port=8001, reload=True)
    Base.metadata.create_all(bind=engine)
