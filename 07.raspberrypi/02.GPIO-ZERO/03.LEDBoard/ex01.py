from gpiozero import LEDBoard
from time import sleep
from signal import pause

leds = LEDBoard(12,16,20,21)

while 1:
    leds.on()
    sleep(1)
    leds.off()
    sleep(1)

