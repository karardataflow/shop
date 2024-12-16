from view import *


class Controller:
    def __init__(self):
        self.view = MyView(self)

    def show_list(self):
        self.show_list_add = Lists(self)
        self.show_list_add.show()
