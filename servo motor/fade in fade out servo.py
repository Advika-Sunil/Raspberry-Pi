import RPi.GPIO as gpio
from time import sleep

gpio.setwarnings(False)
gpio.setmode(gpio.BOARD)
gpio.setup(8,gpio.OUT)

servo_pwm=gpio.PWM(8,50) # pin no , freq
servo_pwm.start(2)#duty cycle for 0 deg

sleep(1)
# for i in range (2,12,1):
#        servo_pwm.ChangeDutyCycle(i)
#        sleep(0.5)
       

for i in range(2, 12, 1):
    servo_pwm.ChangeDutyCycle(i)
    print(i)
    sleep(0.1)

# i = 12
# while i > 2:
#     servo_pwm.ChangeDutyCycle(i)
#     i-=0.5
#     print(i)
#     sleep(0.5)

servo_pwm.stop()
            
