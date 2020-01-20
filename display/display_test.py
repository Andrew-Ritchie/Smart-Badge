from ili934xnew import ILI9341, color565
from machine import Pin, SPI
import glcdfont
import gfx
import time


def randrange(min_value, max_value):
    # Simple randrange implementation for ESP8266 uos.urandom function.
    # Returns a random integer in the range min to max.  Supports only 32-bit
    # int values at most.
    magnitude = abs(max_value - min_value)
    randbytes = uos.urandom(4)
    offset = int((randbytes[3] << 24) | (randbytes[2] << 16) | (
        randbytes[1] << 8) | randbytes[0])
    offset %= (magnitude+1)  # Offset by one to allow max_value to be included.
    return min_value + offset


def fast_hline(x, y, width, color):
    display.fill_rectangle(x, y, width, 1, color)


def fast_vline(x, y, height, color):
    display.fill_rectangle(x, y, 1, height, color)


spi = SPI(1, 40000000, miso=Pin(12), mosi=Pin(13), sck=Pin(14))
display = ILI9341(spi, cs=Pin(18), dc=Pin(19), rst=Pin(5), w=160, h=128, r=7)

graphics = gfx.GFX(160, 128, display.pixel, hline=fast_hline, vline=fast_vline)

display.erase()

for i in range(15):
    x0 = randrange(0, 128)
    y0 = randrange(0, 160)
    x1 = randrange(0, 128)
    y1 = randrange(0, 160)
    r = randrange(0, 255)
    g = randrange(0, 255)
    b = randrange(0, 255)
    graphics.line(x0, y0, x1, y1, color565(r, g, b))

time.sleep_ms(1000)
display.erase()

graphics.fill_triangle(50, 60, 80, 10, 100, 90, color565(r, g, b))

time.sleep_ms(1000)
display.erase()

graphics.fill_circle(60, 60, 20, color565(r, g, b))

time.sleep_ms(1000)
display.erase()

display.print("Hello world!")
