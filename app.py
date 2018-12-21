from devopsmoscow_bot import bot_properties
from telegram.ext import Updater, CommandHandler


updater = Updater(token=bot_properties.TG_BOT_TOKEN, request_kwargs={'read_timeout': 20, 'connect_timeout': 40})
dispatcher = updater.dispatcher


def start(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text="I'm a bot, please talk to me!")


def get_users(bot, update):
    updates = updater.bot.get_updates()
    bot.send_message(chat_id=update.message.chat_id, text=[u.message.text for u in updates])
    # chat = Chat(id=bot_properties.DEVOPS_SUPERGROUP_DETAILS[""])
    # pass


start_handler = CommandHandler('start', start)
users_handler = CommandHandler('users', get_users)
dispatcher.add_handler(start_handler)
dispatcher.add_handler(users_handler)
updater.start_polling()
updater.idle()

