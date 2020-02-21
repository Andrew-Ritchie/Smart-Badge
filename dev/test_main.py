# RELIES ON LITTLEVGL FIRMWARE BEING FLASHED ON ESP32

import lvgl as lv
from main_menu import MainMenuApp
from name import NameApp
from pong import PongApp
from display import Display
import sensors
import time

# Initialise LittlevGL -- for display
lv.init()

# Initialise and register the display
disp = Display()

buttons = sensors.Buttons(up=27, down=33, left=25,
                          right=12, a=35, b=26, x=34, y=32)

MainMenuApp(disp, buttons)
