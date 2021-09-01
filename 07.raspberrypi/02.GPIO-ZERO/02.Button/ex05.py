from gpiozero import LED, Button
from signal import pause

red = LED(13)
btn = Button(26)

red.source = btn

pause()