import lvgl as lv
from widgets import *
import app
import game as g
#import time


class MazeApp(app.GameApp):

    def __init__(self, disp):

        super().__init__("Maze", disp, kill=True)

        self.add_sprite("ball", 10, 10, 4, 2)
