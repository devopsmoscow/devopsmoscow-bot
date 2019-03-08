from trello import TrelloClient

from devopsmoscow_bot import bot_properties
from devopsmoscow_bot.database.sqlalchemy import SqlAlchemy
from devopsmoscow_bot.trello.card import TrelloCard
from devopsmoscow_bot.database.repository import PlatformQuestions, AnnounceQuestions, SpeakerQuestions


class Meetup:

    def __init__(self, meetup_id=None, name=None, description=None, date=None, platform=None):
        self.data = []
        self.meetup_id = meetup_id
        self.name = name
        self.description = description
        self.date = date
        self.platform = platform

    def __get_questions(self, purpose):
        if purpose == "platform":
            repo = PlatformQuestions
        elif purpose == "announce":
            repo = AnnounceQuestions
        elif purpose == "speaker":
            repo = SpeakerQuestions
        else:
            raise Exception("Purpose is incorrect!")
        session = SqlAlchemy().init_session()
        questions = session.query(repo)
        session.close()
        return questions.values("question")

    def new_checklist(self, purpose):
        title = self.name + " meetup в " + self.platform + "чеклист"
        questions = self.__get_questions(purpose)
        items = list()
        for question in questions:
            items.append(question)
        return {'title': title, 'items': items}

    def __create_cards(self):
        card = TrelloCard(name=self.name,
                          description=self.description)
        for purpose in ["platform", "announce", "speaker"]:
            checklist = self.new_checklist(purpose)
            card.checklist(checklist)

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
