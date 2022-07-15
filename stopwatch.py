import machine
import time
import RGB1602

lcd=RGB1602.RGB1602(16,2)

button_top = machine.Pin(14, machine.Pin.IN, machine.Pin.PULL_DOWN)
button_btm = machine.Pin(15, machine.Pin.IN, machine.Pin.PULL_DOWN)

buzzer = machine.PWM(machine.Pin(12))
buzzer.freq(500)

pause = True
count = 0000

def setupLCD():
    lcd.setRGB(255,255,255)
    lcd.setCursor(0,0)
    lcd.printout("Hello World")
    lcd.setCursor(0,1)
    lcd.printout(count)
    

def tick(tmr):
    global count
    global pause
    if not pause:
        count += 1

def int_handler(pin):
    button_top.irq(handler=None)        # temporarily disable interrupts
    button_btm.irq(handler=None)
    
    print("Interrupt Detected!")    
    
    buzzer.duty_u16(500)    # volume
    time.sleep(0.25)                # length
    buzzer.duty_u16(0)
    
    global pause
    if pin == button_top and not pause:
        pause = True
        time.sleep(0.25)
        if button_top.value():
            global count
            count = 0
    elif pin == button_btm and pause:
        pause = False

    time.sleep(0.5)
    button_top.irq(handler=int_handler) # re-enable interrupts
    button_btm.irq(handler=int_handler)
 

button_top.irq(trigger=machine.Pin.IRQ_RISING, handler=int_handler)
button_btm.irq(trigger=machine.Pin.IRQ_RISING, handler=int_handler)     

tim = machine.Timer(period=5000, mode=machine.Timer.ONE_SHOT, callback=lambda t:print(1))
tim.init(period=1000, mode=machine.Timer.PERIODIC, callback=tick)                                                    


setupLCD()
while True: 
        lcd.setCursor(0,1)
        lcd.printout(count)