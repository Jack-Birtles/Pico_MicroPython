from machine import Pin
from machine import PWM
import time

# Set our pin 2 to PWM
pwm = PWM(Pin(13))

pwm.freq(10000)

while 1:
  # Brightness between 0 and 1023
  for brightness in range (0, 65535, 5000):
    pwm.duty_u16(brightness)
    print(brightness)
    time.sleep(0.1)

  # Brightness between 1023 and 0
  for brightness in range (65535, 0, -5000):
    pwm.duty_u16(brightness)
    print(brightness)
    time.sleep(0.1)