import RPi.GPIO as gpio
from time import sleep

gpio.setwarnings(False)
gpio.setmode(gpio.BOARD)
gpio.setup(7,gpio.OUT,initial=gpio.LOW)
gpio.setup(15,gpio.IN,pull_up_down=gpio.PUD_UP)

#using pull up mode - by default gpio is on so led is on
#so we set the else condition to high and if to low
#so when u press the button the led goes off

#by default gpio is high
while True:
    if(gpio.input(15)==gpio.LOW):

        gpio.output(7,gpio.HIGH)
    else:

        gpio.output(7,gpio.LOW)

