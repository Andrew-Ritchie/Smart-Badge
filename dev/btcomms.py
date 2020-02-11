import ble_uart_peripheral as bleuart
import bluetooth
import machine

class BlueComm(object):

    def __init__(self):
        display_name = 'Badge-'+''.join(['{:02x}'.format(b) for b in machine.unique_id()])

        self.ble = bluetooth.BLE()
        self.uart = bleuart.BLEUART(self.ble, name=display_name)

    def irq(self,fn):
        self.uart.irq(handler=fn)

    def read_data(self):
        return self.uart.read().decode()

    def send(self,data):
        self.uart.write(data)

    def __exit__(self):
        self.uart.close()
