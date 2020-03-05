import display as dis
import settings as s
import widgets as w
import app
import lvgl as lv
import time
from display import Display

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

class TimtableApp(app.App):

    def __init__(self, disp):
        super().__init__(name="Timetable", display=disp)
        self.cont = self.get_cont()
        #self.add_item("name", w.Table(self.cont, 3, 3))
        list1 = lv.list(lv.scr_act())
        list1.set_size(160, 200)
        list1.align(None, lv.ALIGN.CENTER, 0, 0)
        list_btn = list1.add_btn(lv.SYMBOL.FILE, "New")
        list_btn.set_event_cb(event_handler)





# x = Timetable()
# x.b
# x.test(x.firstname)
# Initialise LittlevGL -- for display
lv.init()

# Initialise and register the display
disp = Display()

x = TimtableApp(disp)
x.load_screen()

while True:
    time.sleep_ms(1)
