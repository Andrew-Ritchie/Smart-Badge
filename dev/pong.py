import game as g
import time as t
import random


class Ball(g.Sprite):

    #Call the parent class constructor
    def __init__(self):
        super().__init__("ball")

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
        super().__init__("Player", 1, 2)

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
def wait(length_of_time):
    inital = t.time()

    x = False
    while(not(x)):
        current = t.time()
        x = (current - inital) > length_of_time




score1 = 0
score2 = 0

screen = g.Game(6,6, debugger = False)
player1 = Player()
player2 = Player()
ball = Ball()
wall = g.Sprite("wall", 6, 1)
screen.add_sprite(player1, 0,2)
screen.add_sprite(player2, 5,2)
screen.add_sprite(ball, 1,2)
screen.add_sprite(wall, 0,0)
screen.add_sprite(wall, 0,5)
exit_program = False

screen.print()
while not exit_program:
    Ball.bounce(ball, screen.grid)
    screen.move_sprite(ball, ball.direction[0],ball.direction[1])
    Ball.bounce(ball, screen.grid)
    screen.print()
    wait(2)
