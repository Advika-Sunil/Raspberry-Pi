import RPi.GPIO as gpio
from time import sleep

gpio.setwarnings(False)
gpio.setmode(gpio.BOARD)
gpio.setup(3,gpio.OUT,initial=gpio.LOW)
gpio.setup(5,gpio.IN)

while True:
    if(gpio.input(5)==gpio.HIGH):

        gpio.output(3,gpio.HIGH)
    else:

        gpio.output(3,gpio.LOW)
