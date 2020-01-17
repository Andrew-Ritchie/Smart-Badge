from machine import Pin, SPI, I2C
import time
import lis3dh

i2c = I2C(1, scl=Pin(14), sda=Pin(13), freq=4000)
a_sensor = lis3dh.LIS3DH_I2C(i2c)

while True:
    """
    hspi = SPI(1, 1000, sck=Pin(14), mosi=Pin(13), miso=Pin(12))
    cs = Pin(2, Pin.OUT)

    accel_sensor = lis3dh.LIS3DH_SPI(hspi, cs)
    print(accel_sensor.acceleration)

    time.sleep_ms(1)
    """

    print(a_sensor.acceleration, end='\r')
