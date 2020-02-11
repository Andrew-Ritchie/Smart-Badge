import lvgl as lv
from widgets import *
import app
import game as g
import time as t

class Ball(g.Sprite):

    #Call the parent class constructor
    def __init__(self):
        super().__init__("ball",2,2)

        #set spesific parameters
        self.direction = [0,0]
        self.speed = 0
        self.reset()

    def reset(self):
        self.speed = 8.0
        #make this random
        self.direction = [1,1]

    def bounce(self, grid):
        #bounce off player
        print("direction", self.direction)
        print(self.direction[0] + 10)
        print("coords x:", self.x)
        print("coords y:", self.y)
        print(grid[self.x + self.direction[0]][self.y + self.direction[1]])
        if grid[self.x + self.direction[0]][self.y + self.direction[1]] == 1:
            print("oioi")
            if self.direction[0] == 1:
                self.direction[0] = -1
            else:
                self.direction[0] = 1

            if self.direction[1] == 1:
                self.direction[1] = -1
            else:
                self.direction[1] = 1


        #bounce off wall
        if grid[self.x + self.direction[0]][self.y + self.direction[1]] == 3:
            print("hellooooo")


            if self.direction[0] == 1:
                self.direction[0] = -1
            else:
                self.direction[0] = 1




class Player(g.Sprite):
    def __init__(self):
        super().__init__("Player", 1, 5)

    def update(self, dir):
        while True:  # making a loop
            try:  # used try so that if user pressed other than the given key error will not be shown
                if dir == "up":  # if key 'q' is pressed
                    screen.move_sprite(player,0,1)
                if dir == "down":
                    screen.move_sprite(player,0,-1)
                break
            except:
                break  # if user pressed a key other than the given key the loop will break
class Wall(g.Sprite):
    def __init__(self):
        super().__init__(self, "Wall", 1, 2)

#helper function
def pong_wait(length_of_time):
    inital = t.time()

    x = False
    while(not(x)):
        current = t.time()
        x = (current - inital) > length_of_time


class PongApp(app.GameApp):

    def __init__(self, disp):

        super().__init__("Pong", disp)
        score1 = 0
        score2 = 0

        player1 = Player()
        player2 = Player()
        self.ball = Ball()
        wall = g.Sprite("wall", 32, 1)
        self.add_custom_sprite(player1, 0,16)
        self.add_custom_sprite(player2, 31,16)
        self.add_custom_sprite(self.ball, 1,2)
        self.add_custom_sprite(wall, 0,0)
        self.add_custom_sprite(wall, 0,31)

    def run_ball(self):
        while True:
            #Ball.bounce(ball, self.game.grid)
            print("here")
            self.move_sprite("ball", self.ball.direction[0],self.ball.direction[1])
            print("there")
            #Ball.bounce(ball, self.game.grid)
            pong_wait(2)
