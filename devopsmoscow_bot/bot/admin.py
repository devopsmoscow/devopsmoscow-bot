import json
import logging

from telegram import ReplyKeyboardRemove
from telegram.ext import BaseFilter, ConversationHandler

from devopsmoscow_bot import bot_properties
from devopsmoscow_bot.database.repository import GreetingsMessage
from devopsmoscow_bot.database.sqlalchemy import SqlAlchemy


class Admin:

    def __init__(self):
        self.data = []


    @staticmethod
    def new_greetings(bot, update):
        logger = logging.getLogger("deopsmoscow_bot.bot.admin.Admin.new_greetings")
        bot.send_message(chat_id=update.message.chat_id, text="Следующим соообщением отправьте новое приветствие.")
        return "ADD_GREETING"

    @staticmethod
    def add_greetings(bot, update):
        logger = logging.getLogger("deopsmoscow_bot.bot.admin.Admin.add_greetings")
        logger.debug("Got " + str(update.message.text) + " as message!")
        session = SqlAlchemy().init_session()
        session.query(GreetingsMessage).first().update(message=update.message.text)
        session.commit()
        greetings = session.query(GreetingsMessage).first()
        session.close()
        bot.send_message(chat_id=update.message.chat_id, text="Так и записал: " + greetings)
        return ConversationHandler.END

    @staticmethod
    def cancel(bot, update):
        logger = logging.getLogger("deopsmoscow_bot.bot.admin.Admin.cancel")
        user = update.message.from_user
        logger.info("User %s canceled the conversation.", user.first_name)
        update.message.reply_text('Возможно, в другой раз...',
                                  reply_markup=ReplyKeyboardRemove())
        return ConversationHandler.END
