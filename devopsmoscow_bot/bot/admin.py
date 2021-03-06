import json
import logging

from telegram import ReplyKeyboardRemove
from telegram.ext import BaseFilter, ConversationHandler

from devopsmoscow_bot import bot_properties
from devopsmoscow_bot.database.repository import GreetingsMessage
import devopsmoscow_bot.database.repository
from devopsmoscow_bot.database.sqlalchemy import SqlAlchemy


class Admin:

    def __init__(self):
        self.data = []


    @staticmethod
    def new_greetings(bot, update):
        logger = logging.getLogger("deopsmoscow_bot.bot.admin.Admin.new_greetings")
        if update.message.chat_id != bot_properties.GROUP_CHAT_ID:
            session = SqlAlchemy().init_session()
            stored_admin = session.query(devopsmoscow_bot.database.repository.Admin).filter(
                devopsmoscow_bot.database.repository.Admin.id == update.message.from_user.id)
            session.close()
            if not stored_admin.count():
                logger.debug("Access violation for user: " + str(update.message.from_user.username) + ": " + str(update.message.from_user.id))
                bot.send_message(chat_id=update.message.chat_id, text="Вы не админ! Доступ запрещён!")
                return ConversationHandler.END
            else:
                bot.send_message(chat_id=update.message.chat_id, text="Следующим соообщением отправьте новое приветствие.")
                return "ADD_GREETING"

    @staticmethod
    def add_greetings(bot, update):
        logger = logging.getLogger("deopsmoscow_bot.bot.admin.Admin.add_greetings")
        message = update.message.text
        logger.debug("Got " + str(message) + " as message!")
        session = SqlAlchemy().init_session()
        stored_message = session.query(GreetingsMessage).first()
        if not stored_message:
            session.add(GreetingsMessage(message=message))
        else:
            query = session.query(GreetingsMessage).first()
            query.message = message
            session.merge(query)
        session.commit()
        greetings = session.query(GreetingsMessage).first()
        session.close()
        bot.send_message(chat_id=update.message.chat_id, text="Так и записал: " + str(greetings.message))
        return ConversationHandler.END

    @staticmethod
    def cancel(bot, update):
        logger = logging.getLogger("deopsmoscow_bot.bot.admin.Admin.cancel")
        user = update.message.from_user
        logger.info("User %s canceled the conversation.", user.first_name)
        update.message.reply_text('Возможно, в другой раз...',
                                  reply_markup=ReplyKeyboardRemove())
        return ConversationHandler.END

    @staticmethod
    def get_admins(bot, job):
        logger = logging.getLogger("deopsmoscow_bot.bot.admin.Admin.get_admins")
        admins = bot.get_chat_administrators(chat_id=bot_properties.GROUP_CHAT_ID)
        for admin in admins:
            logger.debug(str(admin.user.username) + ": " + str(admin.user.id))
            session = SqlAlchemy().init_session()
            stored_admin = session.query(devopsmoscow_bot.database.repository.Admin).filter(devopsmoscow_bot.database.repository.Admin.id == admin.user.id)
            logger.debug(str(stored_admin))
            if not stored_admin.count():
                session.add(devopsmoscow_bot.database.repository.Admin(id=admin.user.id))
            session.commit()
            session.close()
