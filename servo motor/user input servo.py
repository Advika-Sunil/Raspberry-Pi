import RPi.GPIO as gpio
from time import sleep

gpio.setwarnings(False)
gpio.setmode(gpio.BOARD)
gpio.setup(3,gpio.OUT)

servo_pwm=gpio.PWM(3,50) # pin no , freq
time=1

servo_pwm.start(2)#duty cycle for 0 deg
print("If you want to exit enter -1")
while True:
    
    try:
    
        user=int(input("enter angle between 0 to 180: "))
        duty_cycle=(10*user)//180  #0 to 10 duty cycle
        
        sleep(1)

        if (user<=180 and user>=0):
            servo_pwm.ChangeDutyCycle(duty_cycle+2)
            sleep(time)
            servo_pwm.ChangeDutyCycle(0)
        elif (user==-1):
            
           servo_pwm.stop()
           break
           #exit()
        else:
            print("enter valid input between 0 to 180")
        
            
    except ValueError:
    
        print("please enter only integers")
    

                
