from gpiozero import LED, Button
from signal import pause

btn = Button(26)
red = LED(13)

btn.when_pressed = red.toggle

pause()

