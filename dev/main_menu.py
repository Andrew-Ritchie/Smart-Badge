import lvgl as lv
from widgets import *
import app


class MainMenuApp(app.App):

    def __init__(self, disp):
        th = lv.theme_night_init(210, lv.font_roboto_16)

        super().__init__(name="Main Menu", display=disp, th=th)
        self.set_title("Welcome to SmartBadge!")
        self.cont = self.get_cont()

        self.add_button("Timetable", self.cont.half())
        self.add_button("Maze Game", self.cont.half())
        self.add_button("Pong")
        self.add_button("Name")

    def load_app(self):
        self.load_screen()
