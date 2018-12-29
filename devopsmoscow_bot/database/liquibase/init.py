from pyquibase.pyquibase import Pyquibase
from devopsmoscow_bot import bot_properties


class LiquibaseInit:

    def run_liquibase(self):
        db_url = bot_properties.DB_URL
        db_data = self.parse_url(db_url)
        pyquibase = Pyquibase.postgresql(
            host=db_data['host'],
            port=db_data['port'],
            db_name=db_data['db_name'],
            username=db_data['username'],
            password=db_data['password'],
            change_log_file='db-changelog-1.yml'
        )
        pyquibase.update()

    def parse_url(self, url):
        db_data = dict()
        db_url_list = url.split('/')
        db_data['db_name'] = db_url_list[3]
        main_url_list = db_url_list[2].split('@')
        creds_list = main_url_list[0].split(':')
        db_data['username'] = creds_list[0]
        db_data['password'] = creds_list[1]
        host_list = main_url_list[1].split(':')
        db_data['host'] = host_list[0]
        db_data['port'] = host_list[1]
        return db_data
