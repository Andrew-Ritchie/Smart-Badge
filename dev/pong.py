import game as g
import time as t
import random


class Ball(g.Sprite):

    #Call the parent class constructor
    def __init__(self):
        super().__init__("ball")

        #set spesific parameters
        self.direction = 0
        self.speed = 0
        self.reset()

    def reset(self):
        self.speed = 8.0
        #make this random
        self.direction = (1,0)

    def bounce(self):
        #bounce off player
        if self.grid[self.x + self.direcion[0]][self.y + delf.direcion[1]] == 1:
            if self.direcion[0] == 1:
                self.direcion[0] = -1
            else:
                self.direcion[0] = 1

            numberlist = [-1,0,1]
            self.direcion[1] = random.choice(numberlist)

        #bounce off wall
        if self.grid[self.x + self.direcion[0]][self.y + delf.direcion[1]] == 3:
            if self.direction[1] == 1:
                self.direction = -1
            else:
                self.direction = 1

class Player(g.Sprite):
    def __init__(self):
        super().__init__("Player", 1, 2)

    def update(self, player):
        while True:  # making a loop
            try:  # used try so that if user pressed other than the given key error will not be shown
                if keyboard.is_pressed('w'):  # if key 'q' is pressed
                    r.move_sprite(player,0,-1)
                if keyboard.is_pressed('s'):
                    r.move_sprite(player,0,1)
                break
            except:
                break  # if user pressed a key other than the given key the loop will break
class Wall(g.Sprite):
    def __init__(self):
        super().__init__(self, "Wall", 1, 2)







score1 = 0
score2 = 0

screen = g.Game(6,6, debugger = False)
player1 = Player()
player2 = Player()
ball = Ball()
wall = g.Sprite("wall", 6, 1)
screen.add_sprite(player1, 0,2)
screen.add_sprite(player2, 5,2)
screen.add_sprite(ball, 3,3)
screen.add_sprite(wall, 0,0)
screen.add_sprite(wall, 0,5)
exit_program = False

while not exit_program:
    screen.print()
    break



'''
def start_game():
    r.add_sprite(player1, 0,0)
    r.add_sprite(player2, 5,0)
    r.add_sprite(ball, 3,3)
    r.print()



def wait(length_of_time):
    inital = t.time()

    x = False
    while(not(x)):
        current = t.time()
        x = (current - inital) > length_of_time

def move_ball():
    r.move_sprite(1,0)

r = g.Game(6,6, debugger = False)
player1 = g.Sprite("Player", 1, 2)
player2 = g.Sprite("Player", 1, 2)
ball = g.Sprite("ball", 1, 1)

start_game()
wait(4)
r.move_sprite(ball,1,1)
r.move_sprite(player1, 0,-2)
r.move_sprite(player1, 0, 3)
r.print()

while(ball.x < 7):
    r.move_sprite(ball, 1,1)
    print("oi")
    wait(4)

'''
