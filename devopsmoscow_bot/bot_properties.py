import logging
import os


logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

TG_BOT_TOKEN = os.environ['TG_KEY']
GROUP_CHAT_ID = os.environ['GROUP_CHAT_ID']

DIALOGFLOW_TOKEN = os.environ['DF_TOKEN']

DB_URL = os.environ['DATABASE_URL']

TRELLO_API_KEY = os.environ['TRELLO_API_KEY']
TRELLO_SECRET_KEY = os.environ['TRELLO_SECRET_KEY']
TRELLO_API_TOKEN = os.environ['TRELLO_API_TOKEN']
TRELLO_DEVOPS_BOARD_ID = os.environ['TRELLO_DEVOPS_BOARD_ID']
TRELLO_DEVOPS_IN_PROGRESS_LIST = os.environ['TRELLO_DEVOPS_IN_PROGRESS_LIST']
