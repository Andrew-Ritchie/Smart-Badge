# RELIES ON LITTLEVGL FIRMWARE BEING FLASHED ON ESP32

# Test program to initialise ILI9341 display and register the driver
import lvgl as lv
from display import Display
from widgets import *
from machine import Pin, I2C
import time
#import lis3dh
import sensors

# Set up button input
#b1 = Pin(34, mode=Pin.IN)
buttons = sensors.Buttons(up=27, down=33, left=25,
                          right=12, a=35, b=26, x=34, y=32)

# Set up I2C bus for accelerometer
#i2c = I2C(1, scl=Pin(14), sda=Pin(13), freq=4000)
#a_sensor = lis3dh.LIS3DH_I2C(i2c)
a_sensor = sensors.Accelerometer()

# Initialise LittlevGL
lv.init()

# Initialise communication to display
disp = Display()


# Create a screen
scr = lv.obj()

max_width = scr.get_width()-10

# Create the buttons
# btn = Button(scr, 5, 5, width=max_width, height=20)
# btn.set_text("Option 1")

# btn2 = Button(scr, 5, 35, width=max_width, height=20)
# btn2.set_text("Option 2")

text_buttons = TextArea(scr, 0, 0,  max_width, 60)
text_accelx = TextArea(scr, 0, 60, max_width, 20)
text_accely = TextArea(scr, 0, 80, max_width, 20)
text_accelz = TextArea(scr, 0, 120, max_width, 20)

#line = Line(scr, 10, 10)
#style = line.create_style(colour=(0xff, 0x00, 0x00), width=1, rounded=1)
# line.set_custom_style(style)
# line.set_line_points([{"x": 5, "y": 5},
#                      {"x": 70, "y": 70},
#                      {"x": 100, "y": 10},
#                      {"x": 5, "y": 5}])

while True:
    text_buttons.set_text_content("up={} down={} left={} right={} a={} b={} x={} y={}".format(
        *buttons.get_values()))
    x, y, z = a_sensor.get_values()  # acceleration
    text_accelx.set_text_content(str(x))
    text_accely.set_text_content(str(y))
    text_accelz.set_text_content(str(z))

    lv.scr_load(scr)
    time.sleep_ms(1)
    print('.', end='')
