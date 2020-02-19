import lvgl as lv
from display import Display
from pong import PongApp
import time
import sensors

def testing():
    # Initialise LittlevGL -- for display
    lv.init()

    # Initialise and register the display
    disp = Display()

    pong_app = PongApp(disp)

    return pong_app

