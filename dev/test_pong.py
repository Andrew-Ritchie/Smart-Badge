import lvgl as lv
from display import Display
from maze import MazeApp
import time
import sensors
# Initialise LittlevGL -- for display
lv.init()

# Initialise and register the display
disp = Display()

maze_app = MazeApp(disp)

buttons = sensors.Buttons(up=27, down=33, left=25, right=12, a=35, b=26, x=34, y=32)

def go_up(x):
    maze_app.move_sprite("ball",1,0)
def go_down(x):
    maze_app.move_sprite("ball",-1,0)
def go_left(x):
    maze_app.move_sprite("ball",0,-1)
def go_right(x):
    maze_app.move_sprite("ball",0,1)

buttons.up.set_callback_edge(go_up)
buttons.down.set_callback_edge(go_down)
buttons.left.set_callback_edge(go_left)
buttons.right.set_callback_edge(go_right)

while True:
    print(".", end = "")
    time.sleep_ms(1)
