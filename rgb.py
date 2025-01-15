import RPi.GPIO as gpio
from time import sleep

gpio.setwarnings(False)
gpio.setmode(gpio.BOARD)
gpio.setup(11,gpio.OUT,initial=gpio.LOW)
gpio.setup(13,gpio.OUT,initial=gpio.LOW)
gpio.setup(15,gpio.OUT,initial=gpio.LOW)

gpio.output(11,gpio.HIGH)

sleep(1)
gpio.output(11,gpio.LOW)
sleep(1)

gpio.output(13,gpio.HIGH)
sleep(1)
gpio.output(13,gpio.LOW)
sleep(1)


gpio.output(15,gpio.HIGH)
sleep(1)
gpio.output(15,gpio.LOW)
sleep(1)



