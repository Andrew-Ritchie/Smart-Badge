# RELIES ON LITTLEVGL FIRMWARE BEING FLASHED ON ESP32

# Test program to initialise ILI9341 display and register the driver
import lvgl as lv
from micropython import const
from ili9341 import ili9341
from widgets import Button, TextArea, Line
from machine import Pin, I2C
import time
import lis3dh

# Set up button input
b1 = Pin(34, mode=Pin.IN)

# Set up I2C bus for accelerometer
i2c = I2C(1, scl=Pin(14), sda=Pin(13), freq=4000)
a_sensor = lis3dh.LIS3DH_I2C(i2c)

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
# btn = Button(scr, 5, 5, width=max_width, height=20)
# btn.set_text("Option 1")

# btn2 = Button(scr, 5, 35, width=max_width, height=20)
# btn2.set_text("Option 2")

text_button = TextArea(scr, 5, 65, max_width, 30)
text_accelx = TextArea(scr, 5, 65, max_width, 30)
text_accely = TextArea(scr, 5, 65, max_width, 30)
text_accelz = TextArea(scr, 5, 65, max_width, 30)

#line = Line(scr, 10, 10)
#style = line.create_style(colour=(0xff, 0x00, 0x00), width=1, rounded=1)
#line.set_custom_style(style)
#line.set_line_points([{"x": 5, "y": 5},
#                      {"x": 70, "y": 70},
#                      {"x": 100, "y": 10},
#                      {"x": 5, "y": 5}])

while True:
    text_button.set_text_content("pressed" if b1.value()==1 else "released")
    x,y,z = a_sensor.acceleration
    text_accelx.set_text_content(str(x))
    text_accely.set_text_content(str(y))
    text_accelz.set_text_content(str(z))

    lv.scr_load(scr)
    time.sleep_ms(1)

