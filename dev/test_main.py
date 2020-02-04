# RELIES ON LITTLEVGL FIRMWARE BEING FLASHED ON ESP32

import lvgl as lv
from main_menu import MainMenuApp
from name import NameApp
from display import Display
import sensors
import time

# Initialise LittlevGL -- for display
lv.init()

# Initialise and register the display
disp = Display()

apps = {"main_menu": MainMenuApp(disp), "name": NameApp(disp)}

buttons = sensors.Buttons(up=27, down=33, left=25, right=12, a=35, b=26, x=34, y=32)

curr_group = apps["main_menu"].group

def go_next(x):
    lv.group_focus_next(curr_group)

def go_prev(x):
    lv.group_focus_prev(curr_group)

buttons.right.set_callback_edge(go_next)
buttons.left.set_callback_edge(go_prev)

def main():
    apps['main_menu'].load_screen()
    # time.sleep_ms(10000)
    # apps["name"].load_screen()

main()

while True:
    time.sleep_ms(1)