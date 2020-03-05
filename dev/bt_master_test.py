import btcomms

bt = btcomms.BlueCommMaster()
bt.irq(lambda data: print('Received:', data))

bt.scan()

while not bt.comm._scan_complete:
    ds = bt.detected_devices()
print('Found:', ds)

for i, d in enumerate(ds):
    bt.connect(*d)
    bt.send('Master test' + str(i))
