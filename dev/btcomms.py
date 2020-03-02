import ble_uart_peripheral as bleuart
import ble_temperature_central as blemaster
import bluetooth
import machine

# Temporary
import time

class BlueComm(object):

    def __init__(self, slave=True):
        self.ble = bluetooth.BLE()
        self._slave = slave

        if self._slave:
            display_name = 'Badge-'+''.join(['{:02x}'.format(b) for b in machine.unique_id()])
            self.uart = bleuart.BLEUART(self.ble, name=display_name)
        else:
            self.master = blemaster.BLETemperatureCentral(self.ble)

    def scan(self):
        if self._slave:
            return None
        else:
            detected_devices = []

            def on_scan(addr_type, addr, name):
                if addr_type is not None:
                    nonlocal detected_devices
                    detected_devices.append((self.master._addr_type, self.master._addr))
                    print(detected_devices)
                    #self.master.connect()

            self.master.scan(callback=on_scan)
            return detected_devices

    def connect(self, addr_type, addr):
        if not self._slave:
            self.master._addr_type = addr_type
            self.master._addr = addr

            self.master.connect()

            # Wait for connection...
            while not self.master.is_connected():
                time.sleep_ms(100)

    def irq(self,fn):
        if self._slave:
            self.uart.irq(handler=fn)
        else:
            self.master.on_notify(callback=fn)

    def read_data(self):
        return self.uart.read().decode()

    def send(self,data):
        if self._slave:
            self.uart.write(data)
        else:
            self.master.write(data)

    def __exit__(self):
        self.uart.close()
