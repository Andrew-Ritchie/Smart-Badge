import lvgl as lv
from lib.screen.widgets import *
import lib.app as app
import lib.game.game as g


class MazeApp(app.GameApp):

    def __init__(self, disp):

        super().__init__("Maze", disp)

        self.add_sprite("ball", 10, 10, 4, 2, "BALL")
        #border walls
        self.add_sprite("WALL", 0, 0, 32, 1)
        self.add_sprite("WALL", 1, 0, 1, 32)
        self.add_sprite("WALL", 0, 31, 32, 1)
        #wall with exit
        self.add_sprite("WALL", 1, 31, 1, 17)
        self.add_sprite("WALL", 16, 31, 1, 15)

        #internal walls

        self.add_sprite("WALL", 3, 1, 1, 11)
        self.add_sprite("WALL", 3, 17, 1, 6)
        self.add_sprite("WALL", 3, 25, 1, 11)
        self.add_sprite("WALL", 5, 20, 1, 6)
        self.add_sprite("WALL", 7, 5, 1, 2)
        self.add_sprite("WALL", 15, 31, 1, 17)

