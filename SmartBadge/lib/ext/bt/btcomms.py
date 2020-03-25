import lib.ext.bt.ble_uart_peripheral as bleuart
import lib.ext.bt.ble_central as ble_central
import bluetooth
import machine

# Temporary
import time

class _BlueComm(object):

    def __init__(self):
        self.ble = bluetooth.BLE()
        self.display_name = 'SB'

    def irq(self,fn):
        self.comm.irq(handler=fn)

    def send(self,data):
        self.comm.write(data)

class BlueCommMaster(_BlueComm):

    def __init__(self):
        super().__init__()
        self.comm = ble_central.BLECentral(self.ble)

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
        (Blocking call; waits for scan to terminate)
        Format:
            (<addr_type>, <addr>)
        """
        while not self.comm._scan_complete:
            ds = self.comm.detected_devices()
        return ds

class BlueCommSlave(_BlueComm):

    def __init__(self):
        super().__init__()
        self.comm = bleuart.BLEUART(self.ble, name=self.display_name)

    def __exit__(self):
        self.comm.close()
