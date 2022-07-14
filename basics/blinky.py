import machine
import time
pin = machine.Pin(25, machine.Pin.OUT)
while True:
    pin.value(1)
    time.sleep(1)
    pin.value(0)
    time.sleep(1)