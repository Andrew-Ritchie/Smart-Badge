
import lvgl as lv
from display import Display
from maze import MazeApp

# Initialise LittlevGL -- for display
lv.init()

# Initialise and register the display
disp = Display()

maze_app = MazeApp(disp)
