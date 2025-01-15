import RPi.GPIO as gpio
from time import sleep

gpio.setwarnings(False)
gpio.setmode(gpio.BOARD)
gpio.setup(3,gpio.OUT,initial=gpio.LOW)
gpio.setup(5,gpio.OUT,initial=gpio.LOW)
gpio.setup(7,gpio.OUT,initial=gpio.LOW)
gpio.setup(11,gpio.OUT,initial=gpio.LOW)
gpio.setup(13,gpio.OUT,initial=gpio.LOW)
gpio.setup(15,gpio.OUT,initial=gpio.LOW)
gpio.setup(19,gpio.OUT,initial=gpio.LOW)
#i=0
gpio.setup(21,gpio.IN)
gpio.setup(23,gpio.IN)

    
#     all 5 leds blink at a time

list1 = [3,5,7,11,13,15,19]
#list2 = [19,15,13,11,7,5,3]
while True:
    if(gpio.input(21)==gpio.HIGH):
        
        for i in list1:
            #sleep(1)
            gpio.output(i,gpio.HIGH)
            sleep(1)
            
    if(gpio.input(23)==gpio.HIGH):
        
        for j in range(0,len(list1),-1):
           
            gpio.output(list1[j],gpio.HIGH)
            sleep(1)
           