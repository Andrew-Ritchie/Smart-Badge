import lvgl as lv
from widgets import *
import app


class MainMenuApp(app.App):

    def __init__(self, disp):
        super().__init__(name="Main Menu", display=disp)
        self.set_title("Welcome to SmartBadge!", font_size=28)
        cont = self.get_cont()

        self.add_item("timetable", Button(cont.lv_obj, text="Timetable",
                                          width=cont.half(), app="timetable"), selectable=True)
        self.add_item("maze_game", Button(cont.lv_obj, text="Maze Game",
                                          width=cont.half(), app="maze_game"), selectable=True)
        self.add_item("pong", Button(cont.lv_obj, text="Pong",
                                     width=cont.half(), app="pong"), selectable=True)
        self.add_item("name", Button(cont.lv_obj, text="Name",
                                     width=cont.half(), app="name"), selectable=True)
