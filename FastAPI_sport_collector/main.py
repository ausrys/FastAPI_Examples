from fastapi import FastAPI
import sports
from database import Base, engine
from tasks import scrape_data
import uvicorn

app = FastAPI(title="Sports Scraper API")

# Include router
app.include_router(sports.router)

if __name__ == "__main__":
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)
    Base.metadata.create_all(bind=engine)
    scrape_data()
