import RPi.GPIO as GPIO
import time


red = 13
green = 19

GPIO.setmode(GPIO.BCM)

GPIO.setup(red, GPIO.OUT)
GPIO.setup(green, GPIO.OUT)

try:
    for i in range(10):
        GPIO.output(red,0)
        GPIO.output(green,1)
        time.sleep(1)
        GPIO.output(red,1)
        GPIO.output(green,0)
        time.sleep(1)

except KeyboardInterrupt:
    pass

GPIO.cleanup()