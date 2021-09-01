from gpiozero import Button
from signal import pause

def say_hello():
    print("Hello")

def say_bye():
    print("bye")

btn = Button(26)

btn.when_pressed = say_hello
btn.when_released = say_bye

pause()