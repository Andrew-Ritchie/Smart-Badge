import lib.ext.bt.btcomms as btcomms
import machine

bt = btcomms.BlueCommSlave()
bt.irq(lambda data: bt.send(str(data) + ' ' + str(machine.unique_id())))

print('Running bt_slave_test.py')
