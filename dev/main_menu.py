import lvgl as lv
from micropython import const
from ili9341 import ili9341
from widgets import *

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

th = lv.theme_night_init(210, lv.font_roboto_16)
lv.theme_set_current(th)

cont = Container(scr)

title_text = Label(cont, "Main Menu")

timetable = Button(cont, text="Timetable")
maze_game = Button(cont, text="Maze Game", width=cont.half())
pong = Button(cont, text="Pong", width=cont.half())
about = Button(cont, text="About")

lv.scr_load(scr)
