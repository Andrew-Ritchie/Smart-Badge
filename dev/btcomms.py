import ble_uart_peripheral as btuart
import bluetooth
import machine

class BlueComm(object):

    def __init__(self):
        bt = bluetooth.BLE()
        name = 'SmartBadge-'+''.join(['{:02x}'.format(b) for b in machine.unique_id()])
        self.uart = btuart.BLEUART(bt, name=name)#"SmartBadge-")#{}".format(mac))

    def irq(self,fn):
        self.uart.irq(handler=fn)

    def send(self,data):
        self.uart.write(data)

    def __exit__(self):
        self.uart.close()
