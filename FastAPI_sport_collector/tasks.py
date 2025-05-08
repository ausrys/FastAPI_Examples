from scraper import scrape_sport_news, \
    scrape_sport_events
from models import SportNews, SportEvent
from database import SessionLocal
from celery_app import celery_app


@celery_app.task(name='scrape_data')
def scrape_data():
    db = SessionLocal()
    try:
        news_item = scrape_sport_news()

        news = SportNews(**news_item)
        db.add(news)

        event_item = scrape_sport_events()

        event = SportEvent(**event_item)
        db.add(event)

        db.commit()
    except Exception as e:
        db.rollback()
        print("Error during scraping:", e)
    finally:
        db.close()
