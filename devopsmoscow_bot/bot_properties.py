import logging
import os


logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
TG_BOT_TOKEN = os.environ['TG_KEY']
DEVOPS_SUPERGROUP_DETAILS = {
    "group_title": "DevOps Moscow",
    "username": "devopsmoscow",
    "type": "supergroup"
}
