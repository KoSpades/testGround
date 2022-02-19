from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

DATABASE_URL = "sqlite:///./data_station.db"

engine = create_engine('sqlite://')

Base = declarative_base()
