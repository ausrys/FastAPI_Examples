from scraper import scrape_sport_news, \
    scrape_sport_events
from models import SportNews, SportEvent
from database import SessionLocal
from celery_app import celery_app


@celery_app.task(name='scrape_data')
def scrape_data():
    db = SessionLocal()
    try:
        news_items = scrape_sport_news()

        for item in news_items:
            news = SportNews(**item)
            db.add(news)

        event_items = scrape_sport_events()

        for item in event_items:
            event = SportEvent(**item)
            db.add(event)

        db.commit()
    except Exception as e:
        db.rollback()
        print("Error during scraping:", e)
    finally:
        db.close()
