import lvgl as lv
from widgets import *
import app
import game as g
#import time


class MazeApp(app.GameApp):

    def __init__(self, disp):

        super().__init__("Maze", disp)

        self.add_sprite("ball", 10, 10, 4, 4)

        # rock = GameObj(self.scr, 8, 10, 10, 10, "rock")
        # heart = GameObj(self.scr, 10, 10, 90, 90, "heart")

        # pong = PongBoard(self.scr, 70, 50, 5, 40)
