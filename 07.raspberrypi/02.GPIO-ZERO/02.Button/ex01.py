from gpiozero import Button
from time import sleep


btn = Button(26)

while 1:
    if btn.is_pressed:
        print("pressed")
        sleep(1)
    
    else:
        print("not pressed")
        sleep(1)