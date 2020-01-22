# RELIES ON LITTLEVGL FIRMWARE BEING FLASHED ON ESP32

# Test program to initialise ILI9341 display and register the driver
import lvgl as lv
from micropython import const
from ili9341 import ili9341

# Initialise LittlevGL
lv.init()

# Initialise and register the display
# Registering is handled automatically by this contructor
# Change 'rot' parameter to edit rotation
disp = ili9341(miso=5, mosi=18, clk=19, cs=13,
               dc=12, rst=4, backlight=2, width=128,
               height=160, backlight_on=1, power=14,
               power_on=1, rot=ili9341.MADCTL_MH, invert=False, mhz=30, colormode=ili9341.COLOR_MODE_RGB)

# Create a screen
scr = lv.obj()

# Create a button on the screen and set label
btn = lv.btn(scr)
btn.align(lv.scr_act(), lv.ALIGN.CENTER, 0, 0)
label = lv.label(btn)
label.set_text("Hello World!")

# Load the screen at the end
lv.scr_load(scr)
