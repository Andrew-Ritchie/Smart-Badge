import lvgl as lv
from display import Display
from widgets import *

NIGHT_THEME = lv.theme_night_init(210, lv.font_roboto_16)

class App():

    def __init__(self, name, display, th=NIGHT_THEME):
        self.theme = th
        lv.theme_set_current(self.theme)
        self.scr = lv.obj()
        self.name = name
        self.disp = display
        self.items = {}
        self.cont = Container(self.scr)

    def set_title(self, title, font_size=None):
        self.items['title'] = Label(self.cont, title, font_size=font_size)

    def load_screen(self):
        lv.scr_load(self.scr)

    def add_item(self, name, item):
        self.items[name] = item

    def get_cont(self):
        return self.cont
