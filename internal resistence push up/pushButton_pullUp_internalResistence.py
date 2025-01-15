import RPi.GPIO as gpio
from time import sleep

gpio.setwarnings(False)
gpio.setmode(gpio.BOARD)
gpio.setup(3,gpio.OUT,initial=gpio.LOW)
gpio.setup(5,gpio.OUT,initial=gpio.LOW)
gpio.setup(7,gpio.OUT,initial=gpio.LOW)
gpio.setup(11,gpio.IN,pull_up_down=gpio.PUD_UP)
gpio.setup(13,gpio.IN,pull_up_down=gpio.PUD_UP)
gpio.setup(15,gpio.IN,pull_up_down=gpio.PUD_UP)



#using pull up mode - by default gpio is on so led is on
#so we set the else condition to high and if to low
#so when u press the button the led goes off

#by default gpio is high
while True:
    if(gpio.input(11)==gpio.LOW and gpio.input(13)==gpio.HIGH and gpio.input(15)==gpio.HIGH):

        gpio.output(3,gpio.HIGH)
        print("red")
        
    elif(gpio.input(13)==gpio.LOW and gpio.input(11)==gpio.HIGH and gpio.input(15)==gpio.HIGH) :

        gpio.output(5,gpio.HIGH)
        print("yellow")
        
    elif(gpio.input(15)==gpio.LOW and gpio.input(11)==gpio.HIGH and gpio.input(13)==gpio.HIGH) :

        gpio.output(7,gpio.HIGH)
        print("green")
        
    elif(gpio.input(11)==gpio.LOW and gpio.input(13)==gpio.LOW and gpio.input(15)==gpio.HIGH):

        gpio.output(5,gpio.LOW)
        gpio.output(7,gpio.LOW)
        
        gpio.output(3,gpio.HIGH)
        sleep(0.3)
        gpio.output(3,gpio.LOW)
        sleep(0.3)
        
        print("red blink")
        
    elif(gpio.input(13)==gpio.LOW and gpio.input(15)==gpio.LOW and gpio.input(11)==gpio.HIGH):
       
        
        gpio.output(3,gpio.LOW)
        gpio.output(7,gpio.LOW)
        
        gpio.output(5,gpio.HIGH)
        sleep(0.3)
        gpio.output(5,gpio.LOW)
        sleep(0.3)
        
        print("yellow blink")
        
    elif(gpio.input(15)==gpio.LOW and gpio.input(11)==gpio.LOW and gpio.input(13)==gpio.HIGH):

       
        
        gpio.output(3,gpio.LOW)
        gpio.output(5,gpio.LOW)
        
        gpio.output(7,gpio.HIGH)
        sleep(0.2)
        gpio.output(7,gpio.LOW)
        sleep(0.2)
        
        print("green blink")
    else:
        gpio.output(3,gpio.LOW)
        gpio.output(5,gpio.LOW)
        gpio.output(7,gpio.LOW)