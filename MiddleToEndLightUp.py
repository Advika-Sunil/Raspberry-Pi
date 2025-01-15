import RPi.GPIO as gpio
from time import sleep

gpio.setwarnings(False)
gpio.setmode(gpio.BOARD)
gpio.setup(3,gpio.OUT,initial=gpio.LOW)
gpio.setup(5,gpio.OUT,initial=gpio.LOW)
gpio.setup(7,gpio.OUT,initial=gpio.LOW)
gpio.setup(11,gpio.OUT,initial=gpio.LOW)
gpio.setup(13,gpio.OUT,initial=gpio.LOW)

i=0
for i in range(0,5,1):
    
#    middle light up 1st then the next 2 m so on


    gpio.output(7,gpio.HIGH)
    sleep(1)

    gpio.output(5,gpio.HIGH)

    
    gpio.output(11,gpio.HIGH)

    sleep(1)
    
    gpio.output(3,gpio.HIGH)

    
    gpio.output(13,gpio.HIGH)

    
    sleep(1)

 