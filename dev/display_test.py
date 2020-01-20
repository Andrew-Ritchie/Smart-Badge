from ili9341 import ILI9341
import time

display = ILI9341()
display.erase()

for i in [0, 90, 180, 270]:
    display.erase()
    display.set_rotation(i)
    display.print("Hello {}".format(i))
    time.sleep_ms(1000)
