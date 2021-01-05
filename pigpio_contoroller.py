import pigpio
import time
from contextlib import closing
import struct

pin = 14
pi = pigpio.pi()


def use_pigpio(width):
    pi.servo_pulsewidth(pin,width)


width_value = 1500
use_pigpio()

change_pecentage = 1.0

change_pecentage_count = 1.0

#ここで、何％の出力で回転させるかを決める
with open("/dev/input/js0","rb")as f:
    while True:
        a=f.read(8)
        t,value,code,index=struct.unpack("<ihbb",a)
        print(a)
        print("t: {:10d}ms,value:{:6d},code:{:1d},index{:1d}".format(t,value,code,index))

        

        if index == 2 and value == 1 :
            print("down pecentage")
            change_pecentage = change_pecentage / 2
            change_pecentage_count = change_pecentage_count * 2
        
        if index == 3 and value == 1:
            print("up pecentage")
            change_pecentage_count = change_pecentage_count / 2
            change_pecentage = change_pecentage * 2

            

        if index == 1 and value == 1 and width_value <= 2000:
            width_value = width_value + 500*change_pecetnage
            if width_value > 2500:
                print("over higher limit")
                change_pecentage_count = 1
                use_pigpio(2500)
                

        if index == 0 and value == 1 and width_value >= 1000:
            width_value = width_value - 500*change_pecentage
            if width_value < 500:
                print("over lower llmit")
                change_pecentage_count = 1
                use_pigpio(500)

       