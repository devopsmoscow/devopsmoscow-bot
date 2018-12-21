from devopsmoscow_bot import bot_properties
from telegram.ext import Updater, CommandHandler
from telegram import Chat

updater = Updater(token=bot_properties.TG_BOT_TOKEN, request_kwargs={'read_timeout': 20, 'connect_timeout': 40})
dispatcher = updater.dispatcher


def start(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text="I'm a bot, please talk to me!")


def get_users(bot, update):
    upd = bot.get_chat_members_count(chat_id=bot_properties.DEVOPS_SUPERGROUP_DETAILS["id"])
    bot.send_message(chat_id=update.message.chat_id, text=upd)


start_handler = CommandHandler('start', start)
users_handler = CommandHandler('users', get_users)
dispatcher.add_handler(start_handler)
dispatcher.add_handler(users_handler)
updater.start_polling()
updater.idle()

