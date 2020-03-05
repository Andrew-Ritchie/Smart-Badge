import lvgl as lv
from lib.screen.display import Display
from pong import PongApp
import time
import lib.ext.sensors as sensors
# Initialise LittlevGL -- for display
lv.init()

# Initialise and register the display
disp = Display()

pong_app = PongApp(disp)

buttons = sensors.Buttons(up=27, down=33, left=25, right=12, a=35, b=26, x=34, y=32)

def go_up(x):
     pong_app.move_sprite("Player1",0,1)
def go_down(x):
     pong_app.move_sprite("Player1",0,-1)
def go_left(x):
     pong_app.move_sprite("Player2",0,1)
def go_right(x):
     pong_app.move_sprite("Player2",0,-1)

buttons.left.set_callback_edge(go_up)
buttons.up.set_callback_edge(go_down)
buttons.down.set_callback_edge(go_left)
buttons.right.set_callback_edge(go_right)
print(pong_app.ball.direction)
while True:
    print(pong_app.ball.direction, pong_app.ball.x, pong_app.ball.y)
    print(pong_app.move_ball())
    print(pong_app.ball.direction, pong_app.ball.x, pong_app.ball.y)
    print("\n\n")
    time.sleep_ms(100)
