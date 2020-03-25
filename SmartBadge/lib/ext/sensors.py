from machine import I2C, Pin
import time


class Accelerometer(object):

    def __init__(self,freq=4000, deadzone=1):
        # Minimum setup
        self._i2c = I2C(1, scl=Pin(14), sda=Pin(13), freq=freq)
        self.sensor = lis3dh.LIS3DH_I2C(self._i2c)

        # Set up tilt interrupts
        self._deadzone = deadzone
        self._handler_tilt_f = None
        self._handler_tilt_b = None
        self._handler_tilt_l = None
        self._handler_tilt_r = None
        from machine import Timer
        self._timer = Timer(-1)
        self._timer.init(period=200, mode=Timer.PERIODIC, callback=lambda t: self._timer_callback(t))

    def _timer_callback(self, t):
        deadzone = self._deadzone
        x, y, _ = self.get_values()

        if x < -deadzone:
            self._handler_tilt_l() if self._handler_tilt_l else None
        elif x > deadzone:
            self._handler_tilt_r() if self._handler_tilt_r else None

        if y < -deadzone:
            self._handler_tilt_b() if self._handler_tilt_b else None
        elif y > deadzone:
            self._handler_tilt_f() if self._handler_tilt_f else None

    def irq_tilt_f(self, handler=None):
        self._handler_tilt_f = handler

    def irq_tilt_b(self, handler=None):
        self._handler_tilt_b = handler

    def irq_tilt_l(self, handler=None):
        self._handler_tilt_l = handler

    def irq_tilt_r(self, handler=None):
        self._handler_tilt_r = handler

    def get_values(self):
        return self.sensor.acceleration

    def get_value_x(self):
        return self.sensor.acceleration[0]

    def get_value_y(self):
        return self.sensor.acceleration[1]

    def get_value_z(self):
        return self.sensor.acceleration[2]

class Button(object):

    def __init__(self, pin, active=1):
        """Initialises a pin as a button signal.
        Takes:
            pin: ESP pin number to use as the input
            active: active level to use (1/0 = active high/low), defaults to 1
        """

        self.pin = Pin(pin, mode=Pin.IN, pull=Pin.PULL_DOWN)

        # Set up interrupt to be triggered on the first edge of the input
        self.pin.irq(handler=self._cb_edge, trigger=(
            Pin.IRQ_RISING if active == 1 else Pin.IRQ_FALLING))
        self.callback_edge = (lambda x: None)
        self.last_trigger = time.ticks_ms()

    def get_value(self):
        return self.pin.value()

    def _cb_edge(self, x):
        # Only count the edge if spaced by 0.12ms (switch debounce)
        if time.ticks_diff(time.ticks_ms(), self.last_trigger) > 0.12:
            self.callback_edge(x)
            self.t = time.ticks_ms()
            gc.collect()

    def set_callback_edge(self, fn):
        """Set the callback actions when the button has a rising edge
        takes: `fn`: function with single argument of Pin object experiencing the edge.
        """
        self.callback_edge = fn


class Buttons(object):

    def __init__(self, up, down, left, right, a, b, x, y):
        self.up = Button(up)
        self.down = Button(down)
        self.left = Button(left)
        self.right = Button(right)
        # self.a = Button(a)
        self.b = Button(b)
        # self.x = Button(x)
        self.y = Button(y)

    def get_values(self):
        return map(lambda x: x.get_value(), (self.up, self.down, self.left, self.right,
                self.a, self.b, self.x, self.y))


    def get_value_up(self):
        return self.up.get_value()

    def get_value_down(self):
        return self.down.get_value()

    def get_value_left(self):
        return self.left.get_value()

    def get_value_right(self):
        return self.right.get_value()

    def get_value_a(self):
        return self.a.get_value()

    def get_value_b(self):
        return self.b.get_value()

    def get_value_x(self):
        return self.x.get_value()

    def get_value_y(self):
        return self.y.get_value()
