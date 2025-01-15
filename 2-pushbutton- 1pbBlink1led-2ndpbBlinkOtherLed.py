import RPi.GPIO as gpio
from time import sleep

gpio.setwarnings(False)
gpio.setmode(gpio.BOARD)
gpio.setup(3,gpio.OUT,initial=gpio.LOW)
gpio.setup(7,gpio.OUT,initial=gpio.LOW)

gpio.setup(13,gpio.OUT,initial=gpio.LOW)
gpio.setup(15,gpio.OUT,initial=gpio.LOW)
gpio.setup(5,gpio.IN)
gpio.setup(11,gpio.IN)

while True:
    if(gpio.input(5)==gpio.HIGH):
       

            gpio.output(3,gpio.HIGH)
            gpio.output(7,gpio.HIGH)
            sleep(1)
            gpio.output(3,gpio.LOW)
            gpio.output(7,gpio.LOW)
            sleep(1)
        
    
    elif(gpio.input(11)==gpio.HIGH):
        
            gpio.output(13,gpio.HIGH)
            gpio.output(15,gpio.HIGH)
            
            
            sleep(1)
            gpio.output(13,gpio.LOW)
    
            gpio.output(15,gpio.LOW)
            sleep(1)
        
        

            
        
    else:

        gpio.output(3,gpio.LOW)
        gpio.output(7,gpio.LOW)
        gpio.output(13,gpio.LOW)
        gpio.output(15,gpio.LOW)
