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
    __tablename__ = 'greetings_message'
    id = Column(Integer, primary_key=True)
    message = Column(String)


class Meetup(Base):
    __tablename__ = 'meetups'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(String)
    date = Column(String)
    platform = Column(String)
    registration_url = Column(String)
    max_participants = Column(Integer)
    registered_participants = Column(Integer)
    state = Column(String)


class PlatformQuestions(Base):
    __tablename__ = 'greetings_message'
    id = Column(Integer, primary_key=True)
    question = Column(String)


class AnnounceQuestions(Base):
    __tablename__ = 'greetings_message'
    id = Column(Integer, primary_key=True)
    question = Column(String)
