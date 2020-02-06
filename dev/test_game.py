
import lvgl as lv
from display import Display
from maze import MazeApp
import time
# Initialise LittlevGL -- for display
lv.init()

# Initialise and register the display
disp = Display()

maze_app = MazeApp(disp)

for i in range(10):
    time.sleep_ms(1500)
    maze_app.move_sprite("ball",1,1)
