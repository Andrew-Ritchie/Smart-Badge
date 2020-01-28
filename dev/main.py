# RELIES ON LITTLEVGL FIRMWARE BEING FLASHED ON ESP32

import lvgl as lv
from micropython import const
from ili9341 import ili9341
from widgets import Button, TextArea, Line
from machine import Pin, I2C
import sensors

# Set up button input
buttons = sensors.Buttons(up=27, down=33, left=25, right=12, a=35, b=26, x=34, y=32)

# Set up accelerometer
a_sensor = sensors.Accelerometer()

# Initialise LittlevGL -- for display
lv.init()

# Initialise and register the display
# Registering is handled automatically by this contructor
# Change 'rot' parameter to edit rotation
disp = ili9341(miso=5, mosi=18, clk=19, cs=22,
               dc=4, rst=21, backlight=2, width=160,
               height=128, backlight_on=1, power=23,
               power_on=1, rot=const(0xb0), invert=False, mhz=30, colormode=ili9341.COLOR_MODE_RGB)

# Create a screen
scr = lv.obj()

# TODO Once JSON branch is merged load settings here

def main():
    temp_text = TextArea(scr, 0, 0, 160, 128)
    temp_text.set_text_content("Temporary text")
    lv.scr_load()

while True:
    main()
