from datetime import datetime

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import SessionLocal
from models import SportNews, SportEvent
from tasks import scrape_data


router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/news", summary="Get latest world sport news")
def get_sport_news(db: Session = Depends(get_db)):
    # Fetch the latest news entry from the database
    latest_news = db.query(SportNews).order_by(SportNews.id.desc()).first()

    # If there is no news in the database, return a message
    if latest_news is None:
        return {"message": "No news found."}

    # Return the latest news entry as a dictionary
    return {
        "title": latest_news.title,
        "url": latest_news.url
    }


@router.get("/events", summary="Get upcoming world sport events")
def get_sport_events(db: Session = Depends(get_db)):
    now = datetime.utcnow()
    events = db.query(SportEvent).filter(SportEvent.date >=
                                         now).order_by(SportEvent.date).limit(10).all()
    return events[0]


@router.get("/dev-scrape", summary="Dev-only scrape trigger")
def dev_scrape():
    scrape_data()
    return {"status": "Scraping complete"}
