import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from devopsmoscow_bot import bot_properties

class SqlAlchemy:

    def __init__(self):
        self.data = []

    @staticmethod
    def init_session():
        engine = create_engine(bot_properties.DB_URL)
        session = Session(bind=engine)
        return session
