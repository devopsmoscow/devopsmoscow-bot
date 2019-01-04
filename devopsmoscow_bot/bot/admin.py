import json
import logging

from telegram.ext import BaseFilter

from devopsmoscow_bot import bot_properties
from devopsmoscow_bot.database.repository import GreetingsMessage
from devopsmoscow_bot.database.sqlalchemy import SqlAlchemy


class Admin:

    def __init__(self):
        self.data = []

    @staticmethod
    def new_greetings(bot, update, user_data):
        logger = logging.getLogger("deopsmoscow_bot.bot.admin.Admin.new_greetings")
        logger.debug("Got " + str(user_data) + " as user_data!")
        pass
