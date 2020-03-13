import lvgl as lv
from lib.screen.widgets import *
from timedata import TimeData
from lib.app import App


class EventApp(App):

    def __init__(self, subject, disp, buttons, tim):
        super().__init__(name="Name", display=disp, buttons=buttons,
                         timer=tim)
        self.subject = subject
        cont = self.get_cont()
        cont.set_center()

        first, nick, last = self.get_name()

        self.add_item("Title", Label(cont.lv_obj, first))
        self.add_item("Time", Label(cont.lv_obj, nick, font_size=28))
        self.add_item("Location", Label(cont.lv_obj, last))

        self.load_screen()

    def get_name(self):
        settings = TimeData("timedata.json", self.subject)
        return settings.get_time_data().split(" ")

    # def btn_y(self, x):
    #     from main_menu import MainMenuApp
    #     mm = MainMenuApp(self.disp, self.buttons, self.tim)
