# RELIES ON LITTLEVGL FIRMWARE BEING FLASHED ON ESP32

import lvgl as lv
from main_menu import MainMenuApp
from name import NameApp
from display import Display
import time

# Initialise LittlevGL -- for display
lv.init()

# Initialise and register the display
disp = Display()

apps = {}
apps["main_menu"] = MainMenuApp(disp)
apps["name"] = NameApp(disp)


def main():
    apps["name"].load_screen()
    time.sleep_ms(10000)
    apps['main_menu'].load_screen()


main()
