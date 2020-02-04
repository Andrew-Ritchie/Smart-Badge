import lvgl as lv
from widgets import *
from settings import Settings
import app


class NameApp(app.App):

    def __init__(self, disp):
        super().__init__(name="Name", display=disp)
        self.cont = self.get_cont()
        self.cont.set_center()

        first, nick, last = self.get_name()

        self.add_item("firstname", Label(self.cont, first))
        self.add_item("nickname", Label(self.cont, nick, font_size=28))
        self.add_item("lastname", Label(self.cont, last))

    def get_name(self):
        settings = Settings("settings.json")
        return settings.get_str_name_and_nickname().split(" ")
