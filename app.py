import telegram
from devopsmoscow_bot import bot_properties
from telegram.ext import Updater
from telegram.ext import CommandHandler

bot = telegram.Bot(token=bot_properties.TG_BOT_TOKEN)
print(bot.get_me())

updater = Updater(token=bot_properties.TG_BOT_TOKEN)
dispatcher = updater.dispatcher
dispatcher.add_handler()

def start(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text="I'm a bot, please talk to me!")


start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)
updater.start_polling()
