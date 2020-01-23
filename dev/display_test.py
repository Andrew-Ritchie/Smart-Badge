# RELIES ON LITTLEVGL FIRMWARE BEING FLASHED ON ESP32

# Test program to initialise ILI9341 display and register the driver
import lvgl as lv
from micropython import const
from ili9341 import ili9341
from widgets import Button
import time

# Initialise LittlevGL
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

max_width = scr.get_width()-10

# Create the buttons
btn = Button(scr, 5, 5, width=max_width, height=20)
btn.set_text("Option 1")

btn2 = Button(scr, 5, 35, width=max_width, height=20)
btn2.set_text("Option 2")

btn3 = Button(scr, 5, 65, width=max_width, height=20)
btn3.set_text("Option 3")

btn4 = Button(scr, 5, 95, width=max_width, height=20)
btn4.set_text("Really long option number 4")

lv.scr_load(scr)

time.sleep_ms(1000)
btn.click()
