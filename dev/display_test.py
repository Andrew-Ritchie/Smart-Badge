# RELIES ON LITTLEVGL FIRMWARE BEING FLASHED ON ESP32

# Test program to initialise ILI9341 display and register the driver
import lvgl as lv
from micropython import const
from ili9341 import ili9341
from widgets import Button, TextArea, Line
from machine import Pin, I2C
import time
#import lis3dh
import sensors

# Initialise and register the display
# Registering is handled automatically by this contructor
# Change 'rot' parameter to edit rotation
disp = ili9341(miso=5, mosi=18, clk=19, cs=22,
               dc=4, rst=21, backlight=2, width=160,
               height=128, backlight_on=1, power=23,
               power_on=1, rot=const(0xb0), invert=False, mhz=30, colormode=ili9341.COLOR_MODE_RGB)


# Initialise LittlevGL
lv.init()

# Create a screen
scr = lv.obj()

max_width = scr.get_width()-10

text_buttons = TextArea(scr, 0, 0,  max_width, 60)

def callback(x):
    print('press')
    text_buttons.set_text_content("up={} down={} left={} right={} a={} b={} x={} y={}".format(
        *buttons.get_values()))

# Set up button input
buttons = sensors.Buttons(up=27, down=33, left=25, right=12, a=35, b=26, x=34, y=32)
buttons.y.set_callback_edge(callback)

while True:
    lv.scr_load(scr)
    time.sleep_ms(1)
    print('.', end='')

