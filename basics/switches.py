import machine
import utime
 
button_top = machine.Pin(14, machine.Pin.IN, machine.Pin.PULL_DOWN)
button_btm = machine.Pin(15, machine.Pin.IN, machine.Pin.PULL_DOWN)
 
 
while True:
    
    if button_top.value() == 1:
        print("top")
    
    if button_btm.value() == 1:
        print("btm")
        
    utime.sleep_ms(150)