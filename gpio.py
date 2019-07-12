from gpiozero import LED
from time import sleep

led = LED(17)
led1 = LED(27)
led2 = LED(10)


while True:
    led.on()
    sleep(1)
    led.off()
    sleep(1)
    
    led1.on()
    sleep(1)
    led1.off()
    sleep(1)
    
    led2.on()
    sleep(1)
    led2.off()
    sleep(1)
    
    
    
    
    
    
    
    