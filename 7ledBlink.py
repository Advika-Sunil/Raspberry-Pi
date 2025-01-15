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

    
#     all 5 leds blink at a time
list = [3,5,7,11,13,15,19]

for i in range (5):
    for i in list:
        #sleep(1)
        gpio.output(i,gpio.HIGH)
        sleep(1)
        2




 