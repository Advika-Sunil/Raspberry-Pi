import RPi.GPIO as gpio
from time import sleep

gpio.setwarnings(False)
gpio.setmode(gpio.BOARD)
gpio.setup(7,gpio.OUT,initial=gpio.LOW)
gpio.setup(8,gpio.IN)

while(True):
    if(gpio.input(8)==gpio.HIGH):
        

        
        gpio.output(7,gpio.HIGH)
        print("led on")
    else:
        
        gpio.output(7,gpio.LOW)
        print("led off")
       # sleep(1)
