from micropython import const
from ili9341 import ili9341


class Display(ili9341):

    def __init__(self):
        """ Initialise and register the display
            Registering is handled automatically by this contructor            
        """
        self.display = ili9341(miso=5, mosi=18, clk=19, cs=22,
                               dc=4, rst=21, backlight=2, width=160,
                               height=128, backlight_on=1, power=23,
                               power_on=1, rot=const(0xb0), invert=False, mhz=30, colormode=ili9341.COLOR_MODE_RGB)
