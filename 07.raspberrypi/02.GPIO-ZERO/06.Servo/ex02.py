from gpiozero import Servo
from time import sleep

s = Servo(14, min_pulse_width=0.0004, max_pulse_width=0.0023)   #0~180

while 1:
    s.value = 0
    print("90도")
    sleep(0.5)

    s.value=-1
    print("0도")
    sleep(1)

    s.value=0
    print("90도")
    sleep(1)

    
    s.value=1
    print("180도")
    sleep(1)

