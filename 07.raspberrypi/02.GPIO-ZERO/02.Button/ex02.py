from gpiozero import Button
from time import sleep

btn = Button(26)

while 1:
    btn.wait_for_press()
    print("눌림")
    sleep(1)