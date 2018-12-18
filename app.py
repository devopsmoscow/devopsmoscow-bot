import telegram
import os
from telegram import Bot


bot = telegram.Bot(token=os.environ['TG_KEY'])
print(bot.get_me())
