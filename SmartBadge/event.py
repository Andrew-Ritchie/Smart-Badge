import lvgl as lv
from lib.screen.widgets import *
from timedata import TimeData
from lib.app import App
from main_menu import MainMenuApp
 

class EventApp(App):

    def __init__(self, disp, buttons, tim, subject, slot):
        super().__init__(name="Name", display=disp, buttons=buttons, timer=tim,
                         btn_left=self.btn_left,
                         btn_right=self.btn_right,
                         btn_b=self.btn_b)

        self.subject = "EEE"
        self.slot = slot
        cont = self.get_cont()
        cont.set_center()

        first, nick, last = self.get_data()

        self.add_item("Title", Label(cont.lv_obj, first, font_size=28))
        self.add_item("Time", Label(cont.lv_obj, nick))
        self.add_item("Location", Label(cont.lv_obj, last))

        #self.add_item("Back", Button(cont.lv_obj, text="Back",
                                          #width=cont.half(), app=EventApp), selectable=True)

        #self.add_item("Forward", Button(cont.lv_obj, text="forward",
                                          #width=cont.half(), app=EventApp), selectable=True)

        self.load_screen()



    def btn_left(self, x):
        self.slot -= 1
        focused = lv.group_get_focused(self.group)
        app = self.item_ids[id(focused)].app_name
        ac_app = app(self.disp, self.buttons, self.tim, self.subject, self.slot)        

    def btn_right(self, x):
        self.slot += 1
        focused = lv.group_get_focused(self.group)
        app = self.item_ids[id(focused)].app_name
        ac_app = app(self.disp, self.buttons, self.tim, self.subject, self.slot)

    def btn_b(self, x):
        focused = lv.group_get_focused(self.group)
        app = self.item_ids[id(focused)].app_name
        ac_app = app(self.disp, self.buttons, self.tim)

    def get_data(self):
        slot_num = self.slot + 1
        time_data = TimeData("timedata.json", self.subject, slot_num)
        return time_data.get_time_data().split(" ")
