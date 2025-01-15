import RPi.GPIO as gpio
from time import sleep

gpio.setwarnings(False)
gpio.setmode(gpio.BOARD)
gpio.setup(5,gpio.OUT,initial=gpio.LOW)




gpio.output(5,gpio.HIGH)
print("led on")
   

