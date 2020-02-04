import lvgl as lv
from widgets import *
import app


class MainMenuApp(app.App):

    def __init__(self, disp):
        super().__init__(name="Main Menu", display=disp)
        self.set_title("Welcome to SmartBadge!", font_size=28)
        self.cont = self.get_cont()

        self.add_item("timetable", Button(self.cont, text="Timetable", width=self.cont.half()))
        self.add_item("maze_game", Button(self.cont, text="Maze Game", width=self.cont.half()))
        self.add_item("pong", Button(self.cont, text="Pong"))
        self.add_item("name", Button(self.cont, text="Name"))

    def load_app(self):
        self.load_screen()
