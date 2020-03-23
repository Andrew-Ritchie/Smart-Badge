import btcomms

bt = btcomms.BlueComm()

bt.irq(lambda: bt.send('I received: ' + bt.read_data()))

while True:
    pass
