import machine
import time
led_onboard = machine.Pin("LED", machine.Pin.OUT)
led_onboard1 = machine.Pin(15, machine.Pin.OUT)
while True:
 led_onboard.value(1)
 time.sleep(1)
 led_onboard.value(0)
 time.sleep(1)
 led_onboard1.toggle()
 time.sleep(1)
 
