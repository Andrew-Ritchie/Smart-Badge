import lvgl as lv
from lib.screen.widgets import Button
from lib.app import App
from name import NameApp
from pong import PongMenuApp
from maze import MazeMenuApp


class MainMenuApp(App):

    def __init__(self, disp, buttons, tim):
        super().__init__(name="Main Menu", display=disp, buttons=buttons, timer=tim,
                         btn_left=self.btn_left,
                         btn_right=self.btn_right,
                         btn_b=self.btn_b)
        self.set_title("Welcome to SmartBadge!", font_size=28)

        cont = self.get_cont()

        self.add_item("timetable", Button(cont.lv_obj, text="Timetable",
                                          width=cont.half(), app="timetable"), selectable=True)
        self.add_item("maze_game", Button(cont.lv_obj, text="Maze Game",
                                          width=cont.half(), app=MazeMenuApp), selectable=True)
        self.add_item("pong", Button(cont.lv_obj, text="Pong",
                                     width=cont.half(), app=PongMenuApp), selectable=True)
        self.add_item("name", Button(cont.lv_obj, text="Name",
                                     width=cont.half(), app=NameApp), selectable=True)

        self.load_screen()

    def btn_left(self, x):
        lv.group_focus_prev(self.group)

    def btn_right(self, x):
        lv.group_focus_next(self.group)

    def btn_b(self, x):
        focused = lv.group_get_focused(self.group)
        app = self.item_ids[id(focused)].app_name
        ac_app = app(self.disp, self.buttons, self.tim)
