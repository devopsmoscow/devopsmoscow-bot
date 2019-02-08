from trello import TrelloClient
from devopsmoscow_bot import bot_properties


class TrelloCard:

    def __init__(self, card_id=None, name=None, description=None, checklist=None, date=None, pic_url=None):
        self.data = []
        self.card_id = card_id
        self.name = name
        self.description = description
        self.checklist = checklist
        self.date = date
        self.pic_url = pic_url
        self.client = TrelloClient(
                            api_key=bot_properties.TRELLO_API_KEY,
                            api_secret=bot_properties.TRELLO_SECRET_KEY,
                            token=bot_properties.TRELLO_API_TOKEN,
                        )

    def __get_board(self):
        client = self.client
        all_boards = client.list_boards()
        for board in all_boards:
            if board.id == bot_properties.TRELLO_DEVOPS_BOARD_ID:
                return board

    def __get_list(self):
        board = self.__get_board()
        lists = board.list_lists()
        for board_list in lists:
            if board_list.id == bot_properties.TRELLO_DEVOPS_IN_PROGRESS_LIST:
                return board_list

    def __get_card(self):
        trello_list = self.__get_list()
        cards = trello_list.list_cards()
        for card in cards:
            if card.name == self.name:
                return card

    def __add_checklist(self):
        card = self.__get_card()
        card.add_checklist(title=self.checklist["title"], items=self.checklist["items"])

    def __add_pic(self):
        card = self.__get_card()
        card.attach(url=self.pic_url)

    def create(self):
        list = self.__get_list()
        if self.date is not None:
            list.add_card(name=self.name, desc=self.description, due=self.date)
        else:
            list.add_card(name=self.name, desc=self.description)
        if len(self.checklist) != 0:
            self.__add_checklist()
        if self.pic_url is not None:
            self.__add_pic()
