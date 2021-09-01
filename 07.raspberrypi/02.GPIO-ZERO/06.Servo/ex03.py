from gpiozero import AngularServo
from time import sleep

s = AngularServo(14, min_angle=0, max_angle=180, min_pulse_width=0.0004, max_pulse_width=0.0024)

while 1:
    
    # for i in range(0,180,1):
    #     s.angle = i
    #     sleep(0.05)
    s.angle = 0
    sleep(2)

    s.angle = 90
    sleep(2)

    s.angle = 180
    sleep(2)

    s.angle = 90
    sleep(2)