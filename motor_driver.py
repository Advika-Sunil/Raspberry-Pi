import RPi.GPIO as gpio
from time import sleep
gpio.setwarnings(False)
gpio.setmode(gpio.BOARD)

A1=3
A2=5
EA=7
EB=11
B2=13
B1=15

gpio.setup(3,gpio.OUT,initial=gpio.LOW)
gpio.setup(5,gpio.OUT,initial=gpio.LOW)
gpio.setup(7,gpio.OUT,initial=gpio.LOW)
gpio.setup(11,gpio.OUT,initial=gpio.LOW)
gpio.setup(13,gpio.OUT,initial=gpio.LOW)
gpio.setup(15,gpio.OUT,initial=gpio.LOW)


gpio.output(A1,gpio.LOW)
gpio.output(A2,gpio.HIGH)
gpio.output(EA,gpio.HIGH)
sleep(1)
gpio.cleanup()