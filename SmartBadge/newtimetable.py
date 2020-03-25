import lvgl as lv

from lib.screen.widgets import Button
from lib.app import App
from event import EventApp
from lib.screen.display import Display
import lib.ext.sensors as sensors
from machine import Timer



class TimeTableApp(App):
    def __init__(self, disp, buttons, tim):
        super().__init__(name="Main Menu", display=disp, buttons=buttons, timer=tim,
                         btn_up=self.btn_up,
                         btn_down=self.btn_down,
                         btn_b=self.btn_b)

        cont = self.get_cont()

        self.add_item("Electronics", Button(cont.lv_obj, text="Electronics",
                                    app=EventApp, subject="EEE"), selectable=True)
        self.add_item("Aero", Button(cont.lv_obj, text="Aeronautical",
                                    app=EventApp, subject="Aero"), selectable=True)
        self.add_item("Mech", Button(cont.lv_obj, text="Mechanical",
                                    app=EventApp, subject="Mech"), selectable=True)
        self.add_item("Civil", Button(cont.lv_obj, text="Civil",
                                    app=EventApp, subject="Civil"), selectable=True)

        self.load_screen()

    def btn_up(self, x):
        lv.group_focus_prev(self.group)

    def btn_down(self, x):
        lv.group_focus_next(self.group)

    def btn_b(self, x):
        focused = lv.group_get_focused(self.group)
        app = self.item_ids[id(focused)].app_name
        subject = self.item_ids[id(focused)].subject
        ac_app = app(self.disp, self.buttons, self.tim,subject, slot=0)
