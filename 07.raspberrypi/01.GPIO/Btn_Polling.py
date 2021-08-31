import RPi.GPIO as GPIO
import time

btn = 26
green = 19

GPIO.setmode(GPIO.BCM)

GPIO.setup(btn, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(green, GPIO.OUT)

try:
    while True:
        if GPIO.input(btn) == GPIO.LOW:

            print("Button pushed!")
            GPIO.output(green,1)
            time.sleep(0.1)
            GPIO.output(green,0)
    
        # time.sleep(0.1)

except KeyboardInterrupt:
    pass

GPIO.cleanup()