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
    news = db.query(SportNews).order_by(
        SportNews.published_at.desc()).limit(10).all()
    return [
        {
            "title": item.title,
            "content": item.content,
            "url": item.url,
            "published_at": item.published_at.isoformat()
        }
        for item in news
    ]


@router.get("/events", summary="Get upcoming world sport events")
def get_sport_events(db: Session = Depends(get_db)):
    now = datetime.utcnow()
    events = db.query(SportEvent).filter(SportEvent.date >=
                                         now).order_by(SportEvent.date).limit(10).all()
    return [
        {
            "name": event.name,
            "location": event.location,
            "date": event.date.isoformat(),
            "description": event.description,
            "url": event.url
        }
        for event in events
    ]


@router.get("/dev-scrape", summary="Dev-only scrape trigger")
def dev_scrape():
    scrape_data()
    return {"status": "Scraping complete"}
