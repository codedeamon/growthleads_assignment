from dataclasses import dataclass, asdict
from typing import List, Optional

from sqlalchemy import Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base


# SQLAlchemy setup
Base = declarative_base()

class CountryModel(Base):
    __tablename__ = 'country_info'
    name = Column(String, primary_key=True)
    capital = Column(String)
    region = Column(String)
    subregion = Column(String)
    population = Column(Integer)
    currency = Column(String)


