import machine 
import time
pin = 'LED'
led_Builtin = machine.Pin(pin, machine.Pin.OUT)
led1 = machine.Pin(16, machine.Pin.OUT)
led2 = machine.Pin(17, machine.Pin.OUT)
while True: 
    led_Builtin.value(1) 
    led1.value(0)
    led2.value(1)
    time.sleep(0.1)
    
    led_Builtin.value(0) 
    led1.value(1)
    led2.value(0)
    time.sleep(0.1)