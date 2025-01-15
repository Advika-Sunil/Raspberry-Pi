import RPi.GPIO as gpio
from time import sleep

gpio.setwarnings(False)
gpio.setmode(gpio.BOARD)
gpio.setup(3,gpio.OUT,initial=gpio.LOW)

led_pwm=gpio.PWM(3,100) # pin no , freq
led_pwm.start(0)#duty cycle
sleep(1)
led_pwm.ChangeDutyCycle(25)#duty cycle
sleep(1)
led_pwm.ChangeDutyCycle(50)#duty cycle
sleep(1)
led_pwm.ChangeDutyCycle(75)#duty cycle
sleep(1)
led_pwm.ChangeDutyCycle(100)#duty cycle
sleep(1)
led_pwm.stop()
            