from trello import TrelloClient

from devopsmoscow_bot import bot_properties
from devopsmoscow_bot.database.sqlalchemy import SqlAlchemy
from devopsmoscow_bot.trello.card import TrelloCard
from devopsmoscow_bot.database.repository import PlatformQuestions


class Meetup:

    def __init__(self, meetup_id=None, name=None, description=None, date=None, platform=None):
        self.data = []
        self.meetup_id = meetup_id
        self.name = name
        self.description = description
        self.date = date
        self.platform = platform

    def new_checklist(self, purpose):
        title = self.name + " meetup в " + self.platform + "чеклист"
        if purpose == "platform":
            session = SqlAlchemy().init_session()
            questions = session.query(PlatformQuestions)
            session.close()
        else:
            raise Exception("Purpose is incorrect!")
        items = list()
        for question in questions.values("question"):
            items.append(question)
        return {'title': title, 'items': items}

    def __create_cards(self):
        card = TrelloCard(name=self.name,
                          description=self.description)

    def __create_timepad_event(self):
        pass

    def __create_telegram_chats(self):
        pass

    def __add_to_db(self):
        pass

    def launch(self):
        self.__create_cards()
        self.__create_timepad_event()
        self.__create_telegram_chats()
