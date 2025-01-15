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

gpio.setup(A1,gpio.OUT,initial=gpio.LOW)
gpio.setup(A2,gpio.OUT,initial=gpio.LOW)
gpio.setup(EA,gpio.OUT,initial=gpio.LOW)
gpio.setup(EB,gpio.OUT,initial=gpio.LOW)
gpio.setup(B2,gpio.OUT,initial=gpio.LOW)
gpio.setup(B1,gpio.OUT,initial=gpio.LOW)

EA_pwm=gpio.PWM(EA,1000)#pin,freq

EA_pwm.start(0)

# clockwise
gpio.output(A1,gpio.HIGH)
gpio.output(A2,gpio.LOW)
EA_pwm.ChangeDutyCycle(100) #here the range is 0 to 100 instead of 2 in servo
#gpio.output(EA,gpio.HIGH)
sleep(1)

#stop for 1 sec
EA_pwm.ChangeDutyCycle(0)
#gpio.output(EA,gpio.LOW)
sleep(1)

#Anticlockwise
gpio.output(A1,gpio.LOW)
gpio.output(A2,gpio.HIGH)
EA_pwm.ChangeDutyCycle(100)
# gpio.output(EA,gpio.HIGH)
sleep(1)
gpio.cleanup()