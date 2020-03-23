import lvgl as lv

from lib.app import App, GameApp
import lib.game.game as g
from lib.screen.widgets import Button, Label
from settings import HighScores
from generate_maze import generate_wall_list,reformat_to_line
import gc

class MazeMenuApp(App):

    def __init__(self, disp, buttons, tim):
        super().__init__(name="Maze Menu", display=disp, buttons=buttons, timer=tim,
                         btn_left=self.btn_left,
                         btn_right=self.btn_right,
                         btn_b=self.btn_b,
                         btn_y=self.btn_y)
        self.set_title("Maze Game", font_size=28)

        cont = self.get_cont()

        self.add_item("load_game", Button(
            cont.lv_obj, text="Load Game", app=MazeGameApp), selectable=True)
        self.add_item("high_scores", Button(
            cont.lv_obj, text="High Scores", app=MazeScoresApp), selectable=True)

        self.load_screen()

    def btn_left(self, x):
        lv.group_focus_prev(self.group)

    def btn_right(self, x):
        lv.group_focus_next(self.group)

    def btn_b(self, x):
        focused = lv.group_get_focused(self.group)
        app = self.item_ids[id(focused)].app_name
        ac_app = app(self.disp, self.buttons, self.tim)

    def btn_y(self, x):
        from main_menu import MainMenuApp
        MainMenuApp(self.disp, self.buttons, self.tim)


class MazeScoresApp(App):

    def __init__(self, disp, buttons, tim):
        super().__init__(name="Maze Game Scores", display=disp, buttons=buttons, timer=tim,
                         btn_y=self.btn_y)
        self.set_title("High Scores", font_size=28)

        cont = self.get_cont()

        first, second, third = self.get_high_scores()

        self.add_item("first", Label(cont.lv_obj, first))
        self.add_item("second", Label(cont.lv_obj, second))
        self.add_item("third", Label(cont.lv_obj, third))

        self.load_screen()

    def get_high_scores(self):
        scores = HighScores("high_scores.json", "maze")
        return scores.get_top_three().split(" ")

    def btn_y(self, x):
        MazeMenuApp(self.disp, self.buttons, self.tim)


class MazeGameApp(GameApp):

    def __init__(self, disp, buttons, tim):

        super().__init__("Maze", display=disp, buttons=buttons,  debug=False, roll_over=False, border=False, kill=False,
                         btn_left=self.btn_left,
                         btn_right=self.btn_right,
                         btn_up=self.btn_up,
                         btn_down=self.btn_down,
                         btn_y=self.btn_y)

        self.tim = tim
        self.add_sprite("ball", self.game.x//2-1, self.game.y//2-1, 2, 2, "BALL")
        # border walls
        # wall with exit
        self.load_screen()
        gc.collect()
        # internal walls
        grid = [[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,],
                [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,],
                [1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,0,1,],
                [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,],
                [1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,0,1,],
                [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,],
                [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,],
                [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,],
                [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,],
                [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,],
                [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,],
                [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,],
                [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,],
                [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,],
                [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,],
                [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,],
                [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,],
                [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,],
                [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,],
                [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,],
                [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,],
                [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,],
                [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,],
                [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,],
                [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,],
                [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,],
                [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,],
                [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,],
                [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,0,1,0,0,0,0,0,0,1,],
                [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,],
                [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,],
                [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,],]

        walls = generate_wall_list(grid)
        print(walls)
        print(len(walls))
        print(len(grid), len(grid[0]))
        lines = reformat_to_line(walls)
        i = 0
        for wall in walls:
            i += 1
            self.add_sprite("wall {i}".format(i=i), wall[0], wall[1], wall[2], wall[3], "WALL")

    def btn_up(self, x):
        self.move_sprite("ball", 0, -1)

    def btn_down(self, x):
        self.move_sprite("ball", 0, 1)

    def btn_left(self, x):
        self.move_sprite("ball", -1, 0)

    def btn_right(self, x):
        self.move_sprite("ball", 1, 0)

    def btn_y(self, x):
        MazeMenuApp(self.disp, self.buttons, self.tim)
