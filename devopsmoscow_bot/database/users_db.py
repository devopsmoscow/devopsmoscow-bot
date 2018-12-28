from devopsmoscow_bot.database.repository import User
from devopsmoscow_bot.database.sqlalchemy import SqlAlchemy


class UsersDb:

    def __init__(self):
        self.data = []

    def add_user(self, user_id, allow_notifications):
        user = User(id=user_id, allow_notifications=allow_notifications)
        session = SqlAlchemy.init_session()
        session.add(user)
        session.commit()
        session.close()
