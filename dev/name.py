import lvgl as lv
from widgets import *
from settings import Settings
import app


class NameApp(app.App):

    def __init__(self, disp):
        super().__init__(name="Name", display=disp)
        cont = self.get_cont()
        cont.set_center()

        first, nick, last = self.get_name()

        self.add_item("firstname", Label(cont.lv_obj, first), selectable=True)
        self.add_item("nickname", Label(
            cont.lv_obj, nick, font_size=28), selectable=True)
        self.add_item("lastname", Label(cont.lv_obj, last), selectable=True)

    def get_name(self):
        settings = Settings("settings.json")
        return settings.get_str_name_and_nickname().split(" ")
