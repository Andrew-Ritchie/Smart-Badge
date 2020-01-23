import lvgl as lv
from micropython import const
from ili9341 import ili9341
import time
from machine import Pin


class Button(lv.btn):

    def __init__(self, parent, x, y, width=None, height=None):
        super().__init__(parent)
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        if width and height:
            self.set_size(self.width, self.height)
        self.set_pos(x, y)

    def set_text(self, text):
        label = lv.label(self)
        label.set_long_mode(lv.label.LONG.SROLL_CIRC)
        label.set_width(self.width-10)
        label.set_text(text)
        label.set_align(lv.label.ALIGN.CENTER)

    def click(self):
        self.toggle()
