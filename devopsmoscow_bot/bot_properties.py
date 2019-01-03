import logging
import os


logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
TG_BOT_TOKEN = os.environ['TG_KEY']
DIALOGFLOW_TOKEN = os.environ['DF_TOKEN']
DB_URL = os.environ['DATABASE_URL']
GROUP_CHAT_ID = os.environ['GROUP_CHAT_ID']
