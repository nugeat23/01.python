from gpiozero import LED
import time

red = LED(13)

while True:
    red.on()
    time.sleep(1)
    red.off()
    time.sleep(1)


