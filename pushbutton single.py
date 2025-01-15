import RPi.GPIO as gpio
from time import sleep

gpio.setwarnings(False)
gpio.setmode(gpio.BOARD)
gpio.setup(7,gpio.OUT,initial=gpio.LOW)
gpio.setup(13,gpio.IN,pull_up_down=gpio.PUD_UP)

#using pull up mode - by default gpio is on so led is on
#so we set the else condition to high and if to low
#so when u press the button the led goes off

#by default gpio is high
i = 0
while True:
    if(gpio.input(13)==gpio.LOW):
        i+=1
        print("Button pressed",i+1)

        gpio.output(7,gpio.HIGH)
    else:
        gpio.output(7,gpio.LOW)

