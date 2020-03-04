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


class PongApp(app.GameApp):

    def __init__(self, disp, buttons, tim):

        super().__init__("Pong", display=disp, buttons=buttons, debug=False, roll_over=False, border=False, kill=False,
                         btn_left=self.btn_left,
                         btn_right=self.btn_right,
                         btn_up=self.btn_up,
                         btn_down=self.btn_down,
                         btn_b=self.btn_b)
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
        tim.init(period=250, mode=Timer.PERIODIC,callback=lambda t: self.move_ball())

    def bounce_ball(self):
        Right = self.game.collision_edge(self.ball, 0, 1)
        Left = self.game.collision_edge(self.ball, 0, -1)
        Up = self.game.collision_edge(self.ball, 1, 1)
        Down = self.game.collision_edge(self.ball, 1, -1)

        if (self.ball.x + self.ball.width == 29 or self.ball.x - self.ball.width == 3):
            if self.ball.y + self.ball.height == 29:
                self.ball.direction[1] = -2 
            elif self.ball.y - self.ball.height == 3:
                self.ball.direction[1] = 2 
        else:
            if Right:
                self.ball.direction[0] = -1

                if self.ball.y > self.player_2.y + 2*self.player_2.height//3:
                    print("hit right, going down")
                    self.ball.direction[1] = 1
                elif self.ball.y > self.player_2.y + self.player_2.height//3 :
                    print("seems to think it hit the F***king middle, going across")
                    self.ball.direction[1] = 0
                else:
                    print("hit right, going up")
                    print("seems to think it hit the F***king middle, going across")
                    self.ball.direction[1] = -1

            elif Left:
                self.ball.direction[0] = 1

                if self.ball.y > self.player_1.y + 2*self.player_1.height//3:
                    print("hit left, going up")
                    self.ball.direction[1] = 1
                elif self.ball.y > self.player_1.y +  self.player_1.height//3:
                    print("seems to think it hit the F***king middle, going across")
                    self.ball.direction[1] = 0 
                else:
                    print("hit left, going down")
                    self.ball.direction[1] = -1

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

    def btn_b(self, x):
        from main_menu import MainMenuApp
        mm = MainMenuApp(self.disp, self.buttons, self.tim)
