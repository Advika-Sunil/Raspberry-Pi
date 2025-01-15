import RPi.GPIO as gpio
from time import sleep

gpio.setwarnings(False)
gpio.setmode(gpio.BOARD)
gpio.setup(3,gpio.OUT,initial=gpio.LOW)

led_pwm=gpio.PWM(3,100) # pin no , freq
led_pwm.start(0)#duty cycle

#fade in - lights up
for i in range(0,100):
    sleep(0.05)
    led_pwm.ChangeDutyCycle(i)#duty cycle
'''    
#fade out - lights down
for i in range(100,0,-1):
    sleep(0.05)
    led_pwm.ChangeDutyCycle(i)#duty cycle
    
led_pwm.stop()'''

i=100
while (i>=0):
    sleep(0.05)
    led_pwm.ChangeDutyCycle(i)#duty cycle
    i=i-1
led_pwm.stop()        
