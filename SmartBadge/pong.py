import lvgl as lv
from lib.screen.widgets import *
import lib.app as app
import lib.game.game as g
import time as t
import random as r
from machine import Timer


class Ball(g.Sprite):

    def __init__(self):
        super().__init__("ball", 3, 3, "BALL")
        #self.direction = [[-1,1][r.randint(0,1)], 0]
        self.direction = [1, 1]

    def reset(self):
        self.direction = [[-1, 1][r.randint(0, 1)], r.randint(-1, 1)]


class PongMenuApp(app.App):

    def __init__(self, disp, buttons, tim):
        super().__init__(name="Pong Menu", display=disp, buttons=buttons, timer=tim,
                         btn_left=self.btn_left,
                         btn_right=self.btn_right,
                         btn_b=self.btn_b,
                         btn_y=self.btn_y)
        self.set_title("Pong", font_size=28)

        cont = self.get_cont()

        self.add_item("load_game", Button(
            cont.lv_obj, text="Load Game", app=PongGameApp), selectable=True)
        self.add_item("high_scores", Button(
            cont.lv_obj, text="High Scores", app=PongScoresApp), selectable=True)

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


class PongScoresApp(app.App):

    def __init__(self, disp, buttons, tim):
        super().__init__(name="Pong Scores", display=disp, buttons=buttons, timer=tim,
                         btn_y=self.btn_y)
        self.set_title("High Scores", font_size=28)

        cont = self.get_cont()

        self.add_item("ashwin", Label(cont.lv_obj, "Ashwin"))
        self.add_item("miklas", Label(cont.lv_obj, "Miklas"))
        self.add_item("conor", Label(cont.lv_obj, "Conor"))
        self.add_item("andrew", Label(cont.lv_obj, "Andrew"))
        self.add_item("anwen", Label(cont.lv_obj, "Anwen"))
        self.add_item("martin", Label(cont.lv_obj, "Martin"))

        self.load_screen()

    def btn_y(self, x):
        PongMenuApp(self.disp, self.buttons, self.tim)


class PongGameApp(app.GameApp):

    def __init__(self, disp, buttons, tim):

        super().__init__("Pong", display=disp, buttons=buttons, debug=False, roll_over=False, border=False, kill=False,
                         btn_left=self.btn_left,
                         btn_right=self.btn_right,
                         btn_up=self.btn_up,
                         btn_down=self.btn_down,
                         btn_y=self.btn_y)
        score1 = 0
        score2 = 0
        self.player_1 = self.add_sprite("Player1", 1, 16, 1, 10, typ="PADDLE")
        self.player_2 = self.add_sprite("Player2", 30, 16, 1, 10, typ="PADDLE")
        self.add_sprite("wall", 0, 0, 32, 2, typ="WALL")
        self.add_sprite("wall", 0, 30, 32, 2, typ="WALL")
        self.ball = Ball()
        self.add_custom_sprite(self.ball, 16, 16)
        self.tim = tim

        self.load_screen()
        tim.init(period=250, mode=Timer.PERIODIC,
                 callback=lambda t: self.move_ball())

    def bounce_ball(self):
        Right = self.game.collision_edge(self.ball, 0, 1)
        Left = self.game.collision_edge(self.ball, 0, -1)
        Up = self.game.collision_edge(self.ball, 1, 1)
        Down = self.game.collision_edge(self.ball, 1, -1)

        if (self.ball.x + self.ball.width == 29 or self.ball.x - self.ball.width == 3):
            if self.ball.y + self.ball.height == 29:
                self.ball.direction[1] = -2 - r.randint(0, 5)
            elif self.ball.y - self.ball.height == 3:
                self.ball.direction[1] = 2 + r.randint(0, 5)
        else:
            if Right:
                self.ball.direction[0] = -1

                if self.ball.y > self.player_2.y + self.player_2.height//2 + 1:
                    self.ball.direction[1] = 1
                if self.ball.y < self.player_2.y + self.player_2.height//2 - 1:
                    self.ball.direction[1] = -1
                else:
                    self.ball.direction[1] = 0

            elif Left:
                self.ball.direction[0] = 1

                if self.ball.y > self.player_1.y + self.player_1.height//2 + 1:
                    self.ball.direction[1] = 1
                if self.ball.y < self.player_1.y + self.player_1.height//2 - 1:
                    self.ball.direction[1] = -1
                else:
                    self.ball.direction[1] = 0

            elif Up:
                self.ball.direction[1] = -1
            elif Down:
                self.ball.direction[1] = 1

        return "Collision at Right:{R},Left:{L},Up:{U},Down:{D}".format(R=Right, L=Left, U=Up, D=Down)

    def move_ball(self):
        s = self.bounce_ball()
        self.move_sprite(
            "ball", self.ball.direction[0], self.ball.direction[1])
        return s

    def btn_up(self, x):
        self.move_sprite("Player1", 0, 1)

    def btn_down(self, x):
        self.move_sprite("Player1", 0, -1)

    def btn_left(self, x):
        self.move_sprite("Player2", 0, 1)

    def btn_right(self, x):
        self.move_sprite("Player2", 0, -1)

    def btn_y(self, x):
        PongMenuApp(self.disp, self.buttons, self.tim)
