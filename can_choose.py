#can choose sensor

import RPi.GPIO as GPIO
from time import sleep
from datatime import datetime

sensor_out_recive =
motor1_pwm =
motor1_dir = 
motor2_pwm = 
motor2_dir =

how_times = int(input())
sleep_time = int(input()) #after sensor senses time
interbal = int(input())
#Stick sensor_pin+/- into  2 or 4 and 6


GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

GPIO.setup(sensor_out_recive,GPIO.IN) #recive pin
GPIO.setup(motor1_pwm,GPIO.OUT)
GPIO.setup(motor1_dir,GPIO.OUT)
GPIO.setup(motor2_pwm,GPIO.OUT)
GPIO.setup(motor2_dir,GPIO.OUT)

pdw1 = GPIO.PWM(motor1_pwm,50)
pdw2 = GPIO.PWM(motor2_pwm,50)

try:

    count = 1

    pdw1.start(0)
    pdw2.start(0)

    GPIO.output(motor1_dir,GPIO.HIGH) # HIGH is positive direction
    GPIO.output(motor2_dir,GPIO.HIGH)

    for i in range(100): #first speed up
        pdw1.ChangeDutyCycle(i)
        pdw2.ChangeDutyCycle(i)
        sleep(sleep_time)


    while i < how_times

        if(GPIO.input(sensor_out_recive) == GPIO.HIGH):

            print(str(cnt) +  "times")
            count = count + 1
            sleep(sleep_time)

            for i in range(100,0,-10): #decelerate speed

                pwm1.ChangeDutyCycle(i)
                pdw2.ChangeDutyCycle(i)
                sleep(sleep_time)
            
            if i == 0: # finish decelerate speed

                print("stop,Because sensor sense")
                print("please choose 1 or 2")
                select = int(input()) # select

                if select == 1: #go staright

                    for i in range(100):
            
                        pwm1.ChangeDutyCycle(i)　#up speed
                        pwm2.ChangeDutyCycle(i)
                        sleep(sleep_time)

                if select == 2: # go back

                    GPIO.output(motor1_dir,GPIO.LOW) #change direction
                    GPIO.output(motor2_dir,GPIO.LOW)

                    for i in range(100):# up speed

                        pwm1.ChangeDutyCycle(i)
                        pwm2.ChangeDutyCycle(i)
                        sleep(sleep_time)
                        
        else:

            print(GPIO.input(sensor_out_recive))
            print("go straight")
            sleep(interbal)

    for i range(100,0,-20);

        pdw1.ChangeDutyCycle(i)
        pdw2.ChangeDutyCycle(i)
        print("decelerate speed")

except KeyboardlInterrput:
    print("Interrput CTRL + c")

finally:

    pdw1.stop()
    pdw2.stop()
    GPIO.clenup()
    print("finish clenup")


    

