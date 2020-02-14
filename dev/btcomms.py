import ble_uart_peripheral as bleuart
import ble_temperature_central as blemaster
import bluetooth
import machine

# Temporary
import time

class BlueComm(object):

    def __init__(self, slave=True):
        self.ble = bluetooth.BLE()
        self.slave = slave

        if self.slave:
            display_name = 'Badge-'+''.join(['{:02x}'.format(b) for b in machine.unique_id()])
            self.uart = bleuart.BLEUART(self.ble, name=display_name)
        else:
            self.master = blemaster.BLETemperatureCentral(self.ble)

            not_found = False

            def on_scan(addr_type, addr, name):
                if addr_type is not None:
                    self.master.connect()
                else:
                    nonlocal not_found
                    not_found = True

            self.master.scan(callback=on_scan)

            # Wait for connection...
            while not self.master.is_connected():
                time.sleep_ms(100)
                if not_found:
                    return


    def irq(self,fn):
        if self.slave:
            self.uart.irq(handler=fn)
        else:
            self.master.on_notify(callback=fn)

    def read_data(self):
        return self.uart.read().decode()

    def send(self,data):
        if self.slave:
            self.uart.write(data)
        else:
            self.master.write(data)

    def __exit__(self):
        self.uart.close()
