from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import CountryModel
from settings import *
# Set up logging
import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# SQLAlchemy setup



def insert_data_to_db(data):

    # Database connection parameters
    db_url = f'postgresql://{POSTGRES_USER}:{POSTGRES_PASS}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}'
    engine = create_engine(db_url)
    Session = sessionmaker(bind=engine)
    session = Session()

    # Create tables if they do not exist
    CountryModel.metadata.create_all(engine)

    try:
        for country in data:
            session.add(country)  # merge will insert or update as needed
        session.commit()
    except Exception as err:
        logger.error(f"Database error occurred: {err}")
        session.rollback()

    # Close session
    session.close()