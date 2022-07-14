import machine
import utime
 
led_red = machine.Pin(13, machine.Pin.OUT)
led_internal = machine.Pin(25, machine.Pin.OUT)

led_red.value(0)
led_internal.value(0)
 
button = machine.Pin(14, machine.Pin.IN, machine.Pin.PULL_DOWN)
 
def int_handler(pin):
    button.irq(handler=None)        # temporarily disable interrupts
    print("Interrupt Detected!")    
    led_red.value(1)
    led_internal.value(0)
    utime.sleep(4)
    led_red.value(0)
    button.irq(handler=int_handler) # re-enable interrupts
 
button.irq(trigger=machine.Pin.IRQ_RISING, handler=int_handler) # specifies the interrupt handler
                                                                # to be triggered on the rising edge
 
while True:
     led_internal.toggle()
     utime.sleep(2)