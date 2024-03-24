from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime

Base = declarative_base()

class ConcertInfo(Base):
    __tablename__ = 'info'
    id = Column('ID', Integer, primary_key=True)
    venue = Column('Venue', String, nullable=False)
    headliner = Column('Headliner', String, nullable=False)
    support = Column('Support', String)
    concert_date = Column('Concert_Date', String)
    modified_date = Column('Modified_Date', String)
    create_a_date = Column('Create_A_Date', String)

# Assuming your SQLite database is named 'Concerts.db' and is located in the same directory as your script.
engine = create_engine('sqlite:///../concerts.db')
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

# Create a new concert info object
new_concert = ConcertInfo(
    venue="The Best Venue",
    headliner="Amazing Headliner",
    support="Supporting Act",
    concert_date="2023-05-30",
    modified_date=datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    create_a_date=datetime.now().strftime("%Y-%m-%d %H:%M:%S")
)

# Add the new object to the session and commit it
session.add(new_concert)
session.commit()

