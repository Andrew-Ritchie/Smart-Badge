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


class TextArea(lv.ta):

    def __init__(self, parent, x, y, width, height):
        super().__init__(parent)
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.set_size(self.width, self.height)
        self.set_pos(x, y)
        self.set_cursor_type(lv.CURSOR.NONE)

    def set_text_content(self, text):
        self.set_text_align(lv.label.ALIGN.CENTER)
        self.set_text(text)


class Line(lv.line):

    def __init__(self, parent, x, y, align=lv.ALIGN.CENTER):
        super().__init__(parent)
        self.x = x
        self.y = y
        self.align(None, lv.ALIGN.CENTER, self.x, self.y)
        self.default_style = self.create_style()

    def create_style(self, colour=(0x00, 0x3b, 0x75), width=3, rounded=1):
        style_line = lv.style_t()
        lv.style_copy(style_line, lv.style_plain)
        style_line.line.color = lv.color_make(colour[0], colour[1], colour[2])
        style_line.line.width = width
        style_line.line.rounded = rounded
        return style_line

    def set_custom_style(self, style):
        self.set_style(lv.line.STYLE.MAIN, style)

    def set_line_points(self, points):
        self.set_points(points, len(points))

class Bar(lv.bar):

    def __init__(self, parent, x, y, width=None, height=None):
        # Note that for the 1.8" display, height must be a minimum of 11        
        super().__init__(parent)
        self.x = x
        self.y = y
        self.width = width                    
        self.height = height if height >= 11 else 11
        self.set_size(self.width, self.height)
        self.set_pos(x, y)

    def set_animation_time(self, time):
        self.set_anim_time(time)

    def set_value_animation(self, value, anim):
        # Set anim=True to have an animation and False for static
        self.set_value(value, lv.ANIM.ON if anim else lv.ANIM.OFF)    
