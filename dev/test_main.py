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

apps = {"main_menu": MainMenuApp(disp),
        "name": NameApp(disp)}


buttons = sensors.Buttons(up=27, down=33, left=25,
                          right=12, a=35, b=26, x=34, y=32)

curr_app = apps["main_menu"]
curr_group = curr_app.group


def go_next(x):
    global curr_group
    lv.group_focus_next(curr_group)


def go_prev(x):
    global curr_group
    lv.group_focus_prev(curr_group)


def click(x):
    global curr_app, curr_group
    focused = lv.group_get_focused(curr_group)
    app_name = curr_app.item_ids[id(focused)].app_name
    if app_name in apps:
        apps[app_name].load_screen()
        curr_app = apps[app_name]
        curr_group = curr_app.group


buttons.right.set_callback_edge(go_next)
buttons.left.set_callback_edge(go_prev)
buttons.up.set_callback_edge(click)


def main():
    global curr_group
    apps['main_menu'].load_screen()
    time.sleep_ms(10000)


main()

while True:
    time.sleep_ms(1)
