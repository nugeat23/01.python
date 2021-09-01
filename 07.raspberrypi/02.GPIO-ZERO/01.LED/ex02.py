from gpiozero import LED
from signal import pause

green = LED(19)

green.blink(on_time=0.5, off_time=0.5)

try:
    pause()
except:
    pass

print("end")