from sqlalchemy import Column, Integer, Boolean, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    allow_notifications = Column(Boolean)


class Admin(Base):
    __tablename__ = 'admins'
    id = Column(Integer, primary_key=True)


class GreetingsMessage(Base):
    __tablename__ = 'greetings'
    id = Column(Integer, primary_key=True)
    message = Column(String)
