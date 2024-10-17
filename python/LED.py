import machine
import time
led_onboard = machine.Pin(15, machine.Pin.OUT)
while True:
 led_onboard.toggle()
 time.sleep(0.5)