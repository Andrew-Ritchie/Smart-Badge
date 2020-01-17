from machine import Pin, SPI, I2C
import time
import lis3dh

i2c = I2C(1, scl=Pin(14), sda=Pin(13), freq=4000)
a_sensor = lis3dh.LIS3DH_I2C(i2c)

while True:
    print(a_sensor.acceleration, end='\r')

