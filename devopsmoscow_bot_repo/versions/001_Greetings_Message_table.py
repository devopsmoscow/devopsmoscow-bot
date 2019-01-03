from sqlalchemy import *
from migrate import *

meta = MetaData()

greetings_message = Table(
    'greetings_message', meta,
    Column('id', Integer, primary_key=True),
    Column('message', String()),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    meta.bind = migrate_engine
    greetings_message.create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    meta.bind = migrate_engine
    greetings_message.drop()
