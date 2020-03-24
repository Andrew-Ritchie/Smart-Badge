import lvgl as lv
from lib.screen.widgets import *


class Ball(Circle):

    def __init__(self, parent, width, height, x, y):
        super().__init__(parent, width, height, x, y)
        lv.style_copy(self.circle_style, lv.style_plain)
        self.circle_style.body.radius = lv.RADIUS.CIRCLE
        # self.circle_style.body.grad_color = lv.color_hex(0xff0000)
        # self.circle_style.body.main_color = lv.color_hex(0xff0000)
        # self.circle_style.body.border.color = lv.color_hex(0x0000ff)
        self.circle_style.body.main_color = lv.color_hex(0xffffff)
        self.circle_style.body.grad_color = lv.color_hex(0xc0c0c0)
        self.circle_style.body.border.color = lv.color_hex(0x000000)
        self.circle_style.body.border.width = 2
        self.set_style(self.circle_style)


class PongBoard():

    def __init__(self, parent, width, height, x, y):
        self.x = x
        self.board = Button(parent, x=x, y=y, width=width, height=height)
        self.board_style = lv.style_t()
        lv.style_copy(self.board_style,
                      self.board.lv_obj.get_style(lv.label.STYLE.MAIN))
        self.board_style.body.main_color = lv.color_hex(0x000000)
        self.board_style.body.grad_color = lv.color_hex(0x000000)
        self.board_style.body.shadow.width = 0
        self.board.lv_obj.set_style(lv.label.STYLE.MAIN, self.board_style)

    def move(self, x, y):
        self.board.lv_obj.set_pos(x, y)


class Wall(lv.obj):

    def __init__(self, parent, width, height, x, y):
        super().__init__(parent)
        self.set_size(width*4, height*4)
        self.set_pos(x*4, y*4)


class Grid():

    def __init__(self, parent, width, height, x, y):
        self.rects = []

        for i in range(width):
            for j in range(height):
                self.rects.append(
                    Rectangle(parent, (x+i)*4, (y+j)*4, ((x+i)*4+4), ((y+j)*4)+4))


class GameObj():

    def __init__(self, parent, w, h, x, y, obj):
        self.width = w
        self.height = h
        self.x = x
        self.y = y
        if obj == "rock":
            self.outer_points = self.get_rock_points(w, h, x, y)
        else:
            self.outer_points = self.get_heart_points(w, h, x, y)
        self.outer_line = Line(parent, self.outer_points)
        if obj == "rock":
            self.outer_line.set_custom_style(
                self.outer_line.create_style(colour=(79, 55, 48), width=2))
        else:
            self.outer_line.set_custom_style(
                self.outer_line.create_style(colour=(0xff, 0x14, 0x44), width=1))

    def get_rock_points(self, w, h, x, y):
        return [(x+(w//3), y),
                (x, y+(h//3)),
                (x, y+(2*h//3)),
                (x+1, y+(h-1)),
                (x+(2*w//3), y+(h-1)),
                (x+(w-1), y+(2*h//3)),
                (x+(w-1), y+(h//3)),
                (x+(2*w//3), y),
                (x+(w//3), y)]

    def get_heart_points(self, w, h, x, y):
        return [(x+(w//2), y+(h//5)),
                (x+(2*w//5), y),
                (x+1, y),
                (x, y+(h//5)),
                (x, y+(2*h//5)),
                (x+(w//2), y+(h-1)),
                (x+(w-1), y+(2*h//5)),
                (x+(w-1), y+(h//5)),
                (x+(w-2), y),
                (x+(w-(2*w//5)), y),
                (x+(w//2), y+(h//5))]
