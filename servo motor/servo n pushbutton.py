import RPi.GPIO as gpio
from time import sleep

gpio.setwarnings(False)
gpio.setmode(gpio.BOARD)
gpio.setup(3,gpio.OUT)

red_led=5
green_led=7
pb1=11
pb2=13

gpio.setup(red_led,gpio.OUT,initial=gpio.LOW)
gpio.setup(pb1,gpio.IN,pull_up_down=gpio.PUD_UP)

gpio.setup(green_led,gpio.OUT,initial=gpio.LOW)
gpio.setup(pb2,gpio.IN,pull_up_down=gpio.PUD_UP)

servo_pwm=gpio.PWM(3,50) # pin no , freq
time=1

servo_pwm.start(2)#duty cycle for 0 deg

if(gpio.input(pb1)==gpio.LOW):
    
    servo_pwm.ChangeDutyCycle(2) # move servo to 0 deg
   # sleep(0.09)
    #gpio.output(green_led,gpio.HIGH)  # green light
    
elif(gpio.input(pb2)==gpio.LOW):
    
    servo_pwm.ChangeDutyCycle(12) # move servo to 180 deg   
    sleep(0.09)
    gpio.output(red_led,gpio.HIGH) # red light


         