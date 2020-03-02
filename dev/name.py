import lvgl as lv
from widgets import Label
from settings import Settings
from app import App
import time as t


class NameApp(App):

    def __init__(self, disp, buttons, tim):
        super().__init__(name="Name", display=disp, buttons=buttons,
                         timer=tim,
                         btn_b=self.btn_b)
        cont = self.get_cont()
        cont.set_center()

        first, nick, last = self.get_name()

        self.add_item("firstname", Label(
            cont.lv_obj, first))
        self.add_item("nickname", Label(
            cont.lv_obj, nick, font_size=28))
        self.add_item("lastname", Label(cont.lv_obj, last))

        self.load_screen()

    def get_name(self):
        settings = Settings("settings.json")
        return settings.get_str_name_and_nickname().split(" ")

    def btn_b(self, x):
        from main_menu import MainMenuApp
        mm = MainMenuApp(self.disp, self.buttons, self.tim)
