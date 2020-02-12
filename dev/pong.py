import lvgl as lv
from widgets import *
import app
import game as g
import time as t


class Ball(g.Sprite):

    # Call the parent class constructor
    def __init__(self):
        super().__init__("ball", 3, 3, "BALL")
        self.direction = [0, 0]
        self.speed = 0
        self.reset()

    def reset(self):
        self.speed = 8.0
        # make this random
        self.direction = [1, 1]


class PongApp(app.GameApp):

    def __init__(self, disp):

        super().__init__("Pong", disp)
        score1 = 0
        score2 = 0

        self.add_sprite("Player1", 1, 16, 1, 10, typ="PADDLE")
        self.add_sprite("Player2", 30, 16, 1, 10, typ="PADDLE")
        self.add_sprite("wall", 0, 0, 32, 2)
        self.add_sprite("wall", 0, 30, 32, 2)
        self.ball = Ball()
        self.add_custom_sprite(self.ball, 16, 16)

    def bounce_ball(self):
        if self.game.collision_edge(self.ball, 0, 1):
            self.ball.direction[0] = -1
        elif self.game.collision_edge(self.ball, 0, -1):
            self.ball.direction[0] = 1
        if self.game.collision_edge(self.ball, 1, 1):
            self.ball.direction[1] = -1
        elif self.game.collision_edge(self.ball, 1, -1):
            self.ball.direction[1] = 1

    def move_ball(self):
        self.bounce_ball()
        self.move_sprite(
            "ball", self.ball.direction[0], self.ball.direction[1])
        self.sprite_wait(0.5)
