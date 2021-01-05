#Acceleration_sensor

import RPi.GPIO as GPIO
import datetime
import math
from time import sleep


GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

#Variable declaration
sensor_out_recive = 
motor1_pwm =
motor1_dir =
motor2_pwm =
motor2_dir =
#keep the sensor moving

print("please input choose times")
choose_times = int(input())
print("please input sleep time")
input_sleep = float(input())
print("please input how long top speed time")
how_long_keep = int(input())


GPIO.setup(sensor_out_recive,GPIO.IN)
GPIO.setup(motor1_dir,GPIO.OUT)
GPIO.setup(motor1_pwm,GPIO.OUT)
GPIO.setup(motor2_dir,GPIO.OUT)
GPIO.setup(motor2_pwm,GPIO.OUT)

pwm1 = GPIO.pwm(motor1_pwm,50)
pwm2 = GPIO.pwm(motor2_pwm,50)

pwm1.start(0)
pwm2.start(0)

GPIO.output(motor1_dir,GPIO.HIGH)
GPIO.output(motor2_dir,GPIO.HIGH)

for i in range(choose_times):
    try:

        while True: #infinite up down loop

            print("start up speed")
            
            for k in range(100,-1,-1):
                cos = k*0.01
                sin = math.sqrt(1-(cos*cos))
                pwm1.ChangeDutyCycle(sin)
                pwm2.ChangeDutyCycle(sin)
                print(cos,sin)
                sleep(input_sleep)
                if(GPIO.input(sensor_out_recive) == GPIO.LOW):
                    count_break = count_break + 1
                    break

            sleep(how_long_keep)#keep top speed
            
            print("start down speed")
            
            for k in range(101):
                cos = k*0.01
                sin = math.sqrt(1-(cos*cos))
                pwm1.ChangeDutyCycle(sin)
                pwm2.ChangeDutyCycle(sin)
                print(cos,sin)
                sleep(input_sleep)
                if(GPIO.input(sensor_out_recive) == GPIO.LOW):
                    count_break = count_break + 1
                    break
            
            sleep(how_long_keep)

            if(count_break >= 2):
                print("got out of while loop")
                print("now k is" + str(k))
                print("dutycycle Get closer zero")
                for k in range(k,100,1):#using sin move,dutycycle closter zero
                    cos = k*0.01
                    sin = math.sqrt(1-(cos*cos))
                    pwm1.ChangeDutyCycle(sin)
                    pwm2.ChangeDutyCycle(sin)
                    print(cos,sin)
                    sleep(input_sleep)
                break#this code go out while loop
    
    else:
        choose_action = int(input())
        if choose_action == 1:#go straight
            print("go stright")
            for k in range(100,-1,-1):
                cos = k*0.01
                sin = math.sqrt(1-(cos*cos))
                pwm1.ChangeDutyCycle(sin)
                pwm2.ChangeDutyCycle(sin)
                print(cos,sin)
                sleep(input_sleep)
            sleep(how_long_keep)
        
        if choose_action == 2:#go back
            for k in range(101):
                cos = k*0.01
                sin = math.sqrt(1-(cos*cos))
                pwm1.ChangeDutyCycle(sin)
                pwm2.ChangeDutyCycle(sin)
                print(cos,sin)
                sleep(input_sleep)
                if(GPIO.input(sensor_out_recive) == GPIO.LOW):
                    break
                
            sleep(how_long_keep)
  
    except KeyboardInterrupt:
        print("keyboard Interrupt")

    finally:

        for cos_mainasu  in range(101):

            cos_mainasu = cos_mainasu*0.01
            sin_mainasu= math.sqrt(1-(cos_mainasu*cos_mainasu))
            pwm1.ChangeDutyCycle(sin_mainasu)
            pwm2.ChangeDutyCycle(sin_mainasu)
        print("finish this loop")


pwm1.stop()
pwm2.stop()
GPIO.clenup()
print("finish clenup")