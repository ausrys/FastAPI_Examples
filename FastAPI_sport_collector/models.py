from sqlalchemy import Column, Integer, String, DateTime, Text
from datetime import datetime
from database import Base


class SportNews(Base):
    __tablename__ = "sport_news"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    url = Column(String)


class SportEvent(Base):
    __tablename__ = "sport_events"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    location = Column(String)
    date = Column(DateTime)
    description = Column(Text)
    url = Column(String)
