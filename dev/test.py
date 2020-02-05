import game as g
import time as t

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
r.move_sprite(ball,-1,-1)
r.move_sprite(player1, 0,-2)
r.move_sprite(player1, 0, 3)
r.print()

while(ball.x < 7):
    r.move_sprite(ball, 1,1)
    print("oi")
    wait(4)
