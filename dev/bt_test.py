import ubluetooth

## Constants for bluetooth
from micropython import const
_IRQ_CENTRAL_CONNECT                 = const(1 << 0)
_IRQ_CENTRAL_DISCONNECT              = const(1 << 1)
_IRQ_GATTS_WRITE                     = const(1 << 2)
_IRQ_GATTS_READ_REQUEST              = const(1 << 3)
_IRQ_SCAN_RESULT                     = const(1 << 4)
_IRQ_SCAN_COMPLETE                   = const(1 << 5)
_IRQ_PERIPHERAL_CONNECT              = const(1 << 6)
_IRQ_PERIPHERAL_DISCONNECT           = const(1 << 7)
_IRQ_GATTC_SERVICE_RESULT            = const(1 << 8)
_IRQ_GATTC_CHARACTERISTIC_RESULT     = const(1 << 9)
_IRQ_GATTC_DESCRIPTOR_RESULT         = const(1 << 10)
_IRQ_GATTC_READ_RESULT               = const(1 << 11)
_IRQ_GATTC_WRITE_STATUS              = const(1 << 12)
_IRQ_GATTC_NOTIFY                    = const(1 << 13)
_IRQ_GATTC_INDICATE                  = const(1 << 14)


class Bluetooth(object):

    def __init__(self):
        self.bt = ubluetooth.BLE()
        self.bt.active(True)
        self.bt.irq(lambda event, data: None)

    def set_irq(self, fn):
        self.bt.irq(fn)

    def start_gap_scan(self,time):
        self.bt.gap_scan(time)


def bt_irq(event, data):
    if event == _IRQ_CENTRAL_CONNECT:
        # A central has connected to this peripheral.
        print('CENTRAL_CONNECT: conn_handle={}, addr_type={}, addr={}'.format(*data))
    elif event == _IRQ_CENTRAL_DISCONNECT:
        # A central has disconnected from this peripheral.
        print('CENTRAL_DISCONNECT: conn_handle={}, addr_type={}, addr={}'.format(*data))
    elif event == _IRQ_GATTS_WRITE:
        # A central has written to this characteristic or descriptor.
        print('GATTS_WRITE: conn_handle={}, attr_handle={}'.format(*data))
    elif event == _IRQ_GATTS_READ_REQUEST:
        # A central has issued a read. Note: this is a hard IRQ.
        # Return None to deny the read.
        # Note: This event is not supported on ESP32.
        print('GATTS_READ_REQUEST: conn_handle={}, attr_handle={}'.format(*data))
    elif event == _IRQ_SCAN_RESULT:
        # A single scan result.
        print('SCAN_RESULT: addr_type={}, addr={}, connectable={}, rssi={}, adv_data={}'.format(*data))
    elif event == _IRQ_SCAN_COMPLETE:
        # Scan duration finished or manually stopped.
        print('SCAN_COMPLETE')
    elif event == _IRQ_PERIPHERAL_CONNECT:
        # A successful gap_connect().
        print('PERIPHERAL_CONNECT: conn_handle={}, addr_type={}, addr={}'.format(*data))
    elif event == _IRQ_PERIPHERAL_DISCONNECT:
        # Connected peripheral has disconnected.
        print('PERIPHERAL_DISCONNECT: conn_handle={}, addr_type={}, addr={}'.format(*data))
    elif event == _IRQ_GATTC_SERVICE_RESULT:
        # Called for each service found by gattc_discover_services().
        print('GATTC_SERVICE_RESULT: conn_handle={}, start_handle={}, end_handle={}, uuid={}'.format(*data))
    elif event == _IRQ_GATTC_CHARACTERISTIC_RESULT:
        # Called for each characteristic found by gattc_discover_services().
        print('GATTC_CHARACTERISTIC_RESULT: conn_handle={}, def_handle={}, value_handle={}, properties={}, uuid={}'.format(*data))
    elif event == _IRQ_GATTC_DESCRIPTOR_RESULT:
        # Called for each descriptor found by gattc_discover_descriptors().
        print('GATTC_DESCRIPTOR_RESULT: conn_handle={}, dsc_handle={}, uuid={}'.format(*data))
    elif event == _IRQ_GATTC_READ_RESULT:
        # A gattc_read() has completed.
        print('GATTC_READ_RESULT: conn_handle={}, value_handle={}, char_data={}'.format(*data))
    elif event == _IRQ_GATTC_WRITE_STATUS:
        # A gattc_write() has completed.
        print('GATTC_WRITE_STATUS: conn_handle={}, value_handle={}, status={}'.format(*data))
    elif event == _IRQ_GATTC_NOTIFY:
        # A peripheral has sent a notify request.
        print('GATTC_NOTIFY: conn_handle={}, value_handle={}, notify_data={}'.format(*data))
    elif event == _IRQ_GATTC_INDICATE:
        # A peripheral has sent an indicate request.
        print('GATTC_INDICATE: conn_handle={}, value_handle={}, notify_data={}'.format(*data))

if __name__ == '__main__':
    bt = Bluetooth()
    bt.set_irq(bt_irq)
