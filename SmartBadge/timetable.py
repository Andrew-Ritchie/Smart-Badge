import lib.screen.display as dis
import settings as s
from lib.app import ListApp
import lib.screen.widgets as w
import lib.app
import lvgl as lv
import lib.ext.sensors as sensors
from machine import Timer
import time
from lib.screen.display import Display
from lib.screen.widgets import Button
from lib.screen.widgets import List

"""

def event_handler(obj, event):
    if event == lv.EVENT.CLICKED:
        print("Clicked: %s" % lv.list.get_btn_text(obj))

class Timetable(s.Settings):
    def __init__(self):
        super().__init__("settings.json")
        self.con = self.get_str_name()
        self.bla = "ss"

    def test(self, x):
        print(x)

class TimtableApp(List):

    def __init__(self, disp, buttons, timer ):
        super().__init__(name="Timetable", display=disp, buttons=buttons, timer=timer,
                         btn_up=self.btn_up,
                         btn_down=self.btn_down,
                         btn_b=self.btn_b)
        cont = self.get_cont()
        self.add_item("name", w.Table(self.cont, 3, 3))
        list1 = lv.list(lv.scr_act())
        list1.set_size(160, 200)
        list1.align(None, lv.ALIGN.CENTER, 0, 0)
        list_btn = list1.add_btn(lv.SYMBOL.FILE, "New")
        list_btn.set_event_cb(event_handler)

        # list = List(cont.lv_obj)
        #
        # self.add_item("list", list1)

        self.add_item("timetable", Button(cont.lv_obj, text="Timetable",
                                          app="timetable"), selectable=True)
        self.add_item("maze_game", Button(cont.lv_obj, text="Maze Game",
                                          app="maze_game"), selectable=True)
        self.add_item("pong", Button(cont.lv_obj, text="Pong",
                                     app="PongApp"), selectable=True)
        self.add_item("name", Button(cont.lv_obj, text="Name",
                                     app="NameApp"), selectable=True)
        self.add_item("name", Button(cont.lv_obj, text="Name",
                                     app="NameApp"), selectable=True)

    def btn_up(self, x):
        lv.group_focus_prev(self.group)

    def btn_down(self, x):
        lv.group_focus_next(self.group)

    def btn_b(self, x):
        focused = lv.group_get_focused(self.group)
        app = self.item_ids[id(focused)].app_name
        ac_app = app(self.disp, self.buttons, self.tim)




lv.init()

# Initialise and register the display
disp = Display()
buttons = sensors.Buttons(up=27, down=33, left=25,
                          right=12, a=35, b=26, x=34, y=32)
tim = Timer(-1)


x = TimtableApp(disp, buttons, tim)
x.load_screen()

while True:
    time.sleep_ms(1)
"""


class TimetableApp(ListApp):
    def __init__(self, disp, buttons, tim):
        super().__init__(display=disp, buttons=buttons, timer=tim,
                         btn_left=self.btn_left,
                         btn_right=self.btn_right,
                         btn_b=self.btn_b)
        cont = self.get_cont()
        self.set_title("Welcome to SmartBadge!", font_size=28)

        # list = self.create_list(160, 200)
        # list_btn = self.add_btn(list)
        # list_btn.set_event_cb(self.event_handler)
        # list_btn = self.add_btn(list)
        # list_btn.set_event_cb(self.event_handler)
        # list_btn = self.add_btn(list)
        # list_btn.set_event_cb(self.event_handler)
        list1 = lv.list(lv.scr_act())
        list1.set_size(160, 200)
        list1.align(None, lv.ALIGN.CENTER, 0, 0)
        list_btn = list1.add_btn(lv.SYMBOL.FILE, "New")
        list_btn.set_event_cb(self.event_handler)

        self.load_screen()

    def btn_left(self, x):
        lv.group_focus_prev(self.group)

    def btn_right(self, x):
        lv.group_focus_next(self.group)

    def btn_b(self, x):
        focused = lv.group_get_focused(self.group)
        app = self.item_ids[id(focused)].app_name
        ac_app = app(self.disp, self.buttons, self.tim)
