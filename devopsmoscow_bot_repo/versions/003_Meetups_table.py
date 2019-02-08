from sqlalchemy import *
from migrate import *

meta = MetaData()

meetups = Table(
    'meetups', meta,
    Column('id', Integer, primary_key=True),
    Column('message', String()),
    Column('name', String()),
    Column('description', String()),
    Column('date', String()),
    Column('platform', String()),
    Column('registration_url', String()),
    Column('max_participants', Integer()),
    Column('registered_participants', Integer()),
    Column('state', String())
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    meta.bind = migrate_engine
    meetups.create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    meta.bind = migrate_engine
    meetups.drop()
