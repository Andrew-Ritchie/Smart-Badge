from machine import I2C, Pin
import lis3dh

class Accelerometer(object):
    
    def __init__(self,freq=4000):
        self.sensor = lis3dh.LIS3DH_I2C(I2C(1, scl=Pin(14), sda=Pin(13), freq=freq))

    def get_values(self):
        return self.sensor.acceleration

    def get_value_x(self):
        return self.sensor.acceleration[0]
    
    def get_value_y(self):
        return self.sensor.acceleration[1]
    
    def get_value_z(self):
        return self.sensor.acceleration[2]

class Button(object):

    def __init__(self,pin):
        self.pin = Pin(pin, mode=Pin.IN, pull=Pin.PULL_DOWN)

    def get_value(self):
        return self.pin.value()

class Buttons(object):

    def __init__(self, up, down, left, right, a, b, x, y):
        self.up    = Button(up)
        self.down  = Button(down)
        self.left  = Button(left)
        self.right = Button(right)
        self.a = Button(a)
        self.b = Button(b)
        self.x = Button(x)
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

