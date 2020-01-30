import lvgl as lv
from display import Display
from widgets import *

# Initialise LittlevGL
lv.init()

# Initialise communication to display
disp = Display()

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
