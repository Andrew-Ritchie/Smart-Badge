import btcomms
import machine

bt = btcomms.BlueCommSlave()
bt.irq(lambda data: bt.send(str(data) + ' ' + str(machine.unique_id())))
