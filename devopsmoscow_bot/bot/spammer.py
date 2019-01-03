import json
import logging

import apiai
from telegram.ext import BaseFilter

from devopsmoscow_bot import bot_properties
from devopsmoscow_bot.database.repository import GreetingsMessage
from devopsmoscow_bot.database.sqlalchemy import SqlAlchemy


class Spammer:

    def __init__(self):
        self.data = []

    @staticmethod
    def start(bot, update):
        session = SqlAlchemy().init_session()
        message = GreetingsMessage(message="TEST MESSAGE!")
        session.add(message)
        session.commit()
        greetings = session.query(GreetingsMessage).first()
        session.close()
        bot.send_message(chat_id=update.message.chat_id, text=greetings)

    class NewMember(BaseFilter):
        def filter(self, message):
            if not message.new_chat_members:
                return False
            return True

    @staticmethod
    def add_group(bot, update):
        for members in update.message.new_chat_members:
            logger = logging.getLogger("deopsmoscow_bot.bot.spammer.Spammer.add_group")
            logger.debug("Got " + members.username + " as new user!")
            logger.debug(members)
            bot.send_message(update.message.chat_id, text="@{username} привет! Пожалуйста, отправь  мне /start в ЛС."
                             .format(username=members.username))

    @staticmethod
    def send_welcome(bot, update):
        logger = logging.getLogger("deopsmoscow_bot.bot.spammer.Spammer.send_welcome")
        logger.debug("Messaging user!")
        chat_id = update.message.from_user.id
        logger.debug("Sending message to " + str(chat_id))
        bot.send_message(chat_id=chat_id, text="Hey hi! Ima DevOps Moscow Bot!")

    @staticmethod
    def dialogFlowMessage(bot, update):
        request = apiai.ApiAI(bot_properties.DIALOGFLOW_TOKEN).text_request()
        request.lang = 'ru'
        request.session_id = 'DevOpsMoscowBot'
        request.query = update.message.text
        response_json = json.loads(request.getresponse().read().decode('utf-8'))
        response = response_json['result']['fulfillment']['speech']
        if response:
            bot.send_message(chat_id=update.message.chat_id, text=response)
        elif response and update.message.chat_id == bot_properties.GROUP_CHAT_ID:
            pass
        else:
            bot.send_message(chat_id=update.message.chat_id, text='Я Вас не совсем понял!')
