import lakeside
import time

username = 'dshores16@gmail.com'
password = 'phod-jild-whet-whin'

devices = lakeside.get_devices(username, password)

bulb = lakeside.bulb(devices[1]['address'], devices[1]['code'], devices[1]['type'])
bulb.connect()

brightness = 50

for i in range(25):
    bulb.set_state(power=True, brightness=brightness, temperature = i*4)
    time.sleep(0.25)
    
for i in range(2):
    bulb.set_state(power=True)
    time.sleep(1)
    bulb.set_state(power=False)
    time.sleep(1)

switch = lakeside.switch(devices[4]['address'], devices[4]['code'], devices[4]['type'])
switch.connect()

for i in range(2):
    switch.set_state(power=True)
    time.sleep(1)
    switch.set_state(power=False)
    time.sleep(1)
    


