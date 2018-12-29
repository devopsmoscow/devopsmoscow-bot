from devopsmoscow_bot import bot_properties
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from devopsmoscow_bot.bot.spammer import Spammer
import logging

from devopsmoscow_bot.database.liquibase.init import LiquibaseInit

#LiquibaseInit().run_liquibase()

updater = Updater(token=bot_properties.TG_BOT_TOKEN, request_kwargs={'read_timeout': 20, 'connect_timeout': 40})
dispatcher = updater.dispatcher

start_handler = CommandHandler(command='start', callback=Spammer.start)
welcome_handler = CommandHandler(command='welcome', callback=Spammer.send_welcome)
add_group_handler = MessageHandler(callback=Spammer.add_group, filters=Spammer.NewMember())
text_message_handler = MessageHandler(Filters.text, Spammer.dialogFlowMessage)

dispatcher.add_handler(start_handler)
dispatcher.add_handler(welcome_handler)
dispatcher.add_handler(add_group_handler)
dispatcher.add_handler(text_message_handler)

updater.start_polling()
updater.idle()

