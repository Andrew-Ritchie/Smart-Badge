import lvgl as lv
from lib.app import GameApp
import lib.game.game as g


class MazeApp(GameApp):

    def __init__(self, disp, buttons, tim):

        super().__init__("Maze", display=disp, buttons=buttons,  debug=False, roll_over=False, border=False, kill=False,
                         btn_left=self.btn_left,
                         btn_right=self.btn_right,
                         btn_up=self.btn_up,
                         btn_down=self.btn_down,
                         btn_b=self.btn_b)

        self.tim = tim
        self.add_sprite("ball", 10, 10, 2, 2, "BALL")
        # border walls
        self.add_sprite("t_wall", 0, 0, 32, 1, "WALL")
        self.add_sprite("l_wall", 0, 0, 1, 32, "WALL")
        self.add_sprite("b_wall", 0, 31, 32, 1, "WALL")
        # wall with exit
        self.add_sprite("r_wall1", 31, 0, 1, 17, "WALL")
        self.add_sprite("r_wall2", 31, 20, 1, 13, "WALL")

        self.load_screen()

        # internal walls

        # self.add_sprite("WALL", 3, 1, 1, 11)
        # self.add_sprite("WALL", 3, 17, 1, 6)
        # self.add_sprite("WALL", 3, 25, 1, 11)
        # self.add_sprite("WALL", 5, 20, 1, 6)
        # self.add_sprite("WALL", 7, 5, 1, 2)
        # self.add_sprite("WALL", 15, 31, 1, 17)

    def btn_up(self, x):
        self.move_sprite("ball", 0, -1)

    def btn_down(self, x):
        self.move_sprite("ball", 0, 1)

    def btn_left(self, x):
        self.move_sprite("ball", -1, 0)

    def btn_right(self, x):
        self.move_sprite("ball", 1, 0)

    def btn_b(self, x):
        from main_menu import MainMenuApp
        mm = MainMenuApp(self.disp, self.buttons, self.tim)
