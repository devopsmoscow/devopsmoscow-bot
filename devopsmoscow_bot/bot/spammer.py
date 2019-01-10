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
        if update.message.chat_id != bot_properties.GROUP_CHAT_ID:
            session = SqlAlchemy().init_session()
            greetings = session.query(GreetingsMessage).first()
            session.close()
            bot.send_message(chat_id=update.message.chat_id, text=greetings.message)

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
        logger.debug(bot.getMe().username)
        bot.send_message(chat_id=chat_id, text="Hey hi! Ima DevOps Moscow Bot!")

    @staticmethod
    def dialog_flow_message(bot, update):
        logger = logging.getLogger("deopsmoscow_bot.bot.spammer.Spammer.dialog_flow_message")
        mention = "@" + bot.getMe().username
        if (update.message.text.find(mention) != -1) or (update.message.chat_id != bot_properties.GROUP_CHAT_ID):
            logger.debug("Processing with DialogFlow")
            request = apiai.ApiAI(bot_properties.DIALOGFLOW_TOKEN).text_request()
            request.lang = 'ru'
            request.session_id = 'DevOpsMoscowBot'
            request.query = update.message.text
            response_json = json.loads(request.getresponse().read().decode('utf-8'))
            response = response_json['result']['fulfillment']['speech']
            if response:
                try:
                    logger.debug(str(response))
                except Exception as e:
                    pass
                bot.send_message(chat_id=update.message.chat_id, text=response)
            elif not response and update.message.chat_id == bot_properties.GROUP_CHAT_ID:
                pass
            else:
                bot.send_message(chat_id=update.message.chat_id, text='Я Вас не совсем понял!')
        else:
            logger.debug("Found '@' character - ignoring message.")
