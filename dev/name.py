import lvgl as lv
from widgets import *
from settings import Settings
import app


class NameApp(app.App):

    def __init__(self, disp):
        th = lv.theme_night_init(210, lv.font_roboto_28)
        super().__init__(name="Name", display=disp, th=th)
        self.cont = self.get_cont()

        first, nick, last = self.get_name()

        self.add_item(Label(self.cont, first))
        self.add_item(Label(self.cont, nick))
        self.add_item(Label(self.cont, last))

    def load_app(self):
        self.load_screen()

    def get_name(self):
        settings = Settings("settings.json")
        return settings.get_str_name_and_nickname().split(" ")
