from gpiozero import Servo
from time import sleep

s = Servo(14)

while 1:
    s.mid()
    print("중간")
    sleep(0.5)

    s.min()
    print("최소")
    sleep(1)

    s.mid()
    print("중간")
    sleep(0.5)

    s.max()
    print("최대")
    sleep(1)