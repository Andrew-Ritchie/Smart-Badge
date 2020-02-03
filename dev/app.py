import lvgl as lv
from display import Display
from widgets import *


class App():

    def __init__(self, name, display, th=None):
        self.theme = th
        if self.theme:
            lv.theme_set_current(self.theme)
        self.scr = lv.obj()
        self.name = name
        self.disp = display
        self.items = []
        self.cont = Container(self.scr)

    def set_title(self, title):
        self.items.append(Label(self.cont, title))

    def load_screen(self):
        lv.scr_load(self.scr)

    def add_item(self, item):
        self.items.append(item)

    def add_button(self, text, width=None):
        self.items.append(
            Button(self.cont, text=text, width=width))

    def get_cont(self):
        return self.cont
