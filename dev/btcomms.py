import ble_uart_peripheral as bleuart
import ble_temperature_central as blemaster
import bluetooth
import machine

# Temporary
import time

class BlueComm(object):

    def __init__(self):
        self.ble = bluetooth.BLE()
        # self.display_name = 'Badge-'+''.join(['{:02x}'.format(b) for b in machine.unique_id()])
        self.display_name = ''.join(['{:02x}'.format(b) for b in machine.unique_id()])
        self.display_name = self.display_name[-4:]

    def irq(self,fn):
        self.comm.irq(handler=fn)

    def send(self,data):
        self.comm.write(data)

    # def __exit__(self):
    #     self.uart.close()

class BlueCommMaster(BlueComm):

    def __init__(self):
        super().__init__()
        self.comm = blemaster.BLECentral(self.ble)

    def connect(self, addr_type, addr):
        """Connect to a discovered device
        Provide with element from list returned by `detected_devices()`
        e.g. `foo.connect(*foo.detected_devices()[0])`
        """
        self.comm._addr_type = addr_type
        self.comm._addr = addr

        self.comm.connect()

        # Wait for connection...
        while not self.comm.is_connected():
            time.sleep_ms(100)

    def scan(self):
        self.comm.scan()

    def detected_devices(self):
        """Returns list of detected devices
        Format:
            (<addr_type>, <addr>)
        """
        return self.comm.detected_devices()

class BlueCommSlave(BlueComm):

    def __init__(self):
        super().__init__()
        self.comm = bleuart.BLEUART(self.ble, name=self.display_name)
