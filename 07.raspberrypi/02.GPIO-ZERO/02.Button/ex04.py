from gpiozero import LED, Button
from signal import pause

red = LED(13)
btn = Button(26)

btn.when_pressed = red.on
btn.when_released = red.off

pause()