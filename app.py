from devopsmoscow_bot import bot_properties
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, ConversationHandler
from devopsmoscow_bot.bot.spammer import Spammer
from devopsmoscow_bot.bot.admin import Admin
import migrate.versioning.api
import migrate.exceptions
import logging

try:
    migrate.versioning.api.version_control(url=bot_properties.DB_URL, repository='./devopsmoscow_bot_repo')
except migrate.exceptions.DatabaseAlreadyControlledError as e:
    pass
migrate.versioning.api.upgrade(url=bot_properties.DB_URL, repository='./devopsmoscow_bot_repo')

updater = Updater(token=bot_properties.TG_BOT_TOKEN, request_kwargs={'read_timeout': 20, 'connect_timeout': 40})
dispatcher = updater.dispatcher
job_queue = updater.job_queue

start_handler = CommandHandler(command='start', callback=Spammer.start)
welcome_handler = CommandHandler(command='welcome', callback=Spammer.send_welcome)
greetings_update_handler = ConversationHandler(
    entry_points=[CommandHandler('new_greetings', Admin.new_greetings)],
    states={
        "ADD_GREETING": [MessageHandler(Filters.text, Admin.add_greetings)]
    },
    fallbacks=[CommandHandler('cancel', Admin.cancel)]
)
add_group_handler = MessageHandler(callback=Spammer.add_group, filters=Spammer.NewMember())
text_message_handler = MessageHandler(Filters.text, Spammer.dialogFlowMessage)
admin_sync_queue = job_queue.run_repeating(Admin.get_admins, interval=60, first=0)

dispatcher.add_handler(start_handler)
dispatcher.add_handler(welcome_handler)
dispatcher.add_handler(add_group_handler)
dispatcher.add_handler(greetings_update_handler)
dispatcher.add_handler(text_message_handler)

updater.start_polling()
updater.idle()

