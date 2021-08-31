import RPi.GPIO as GPIO
import time

red = 13
green = 19

GPIO.setmode(GPIO.BCM)

GPIO.setup(red, GPIO.OUT)

p = GPIO.PWM(red,50)    # GPIO 핀 설정, 주파수 = 50Hz
p.start(0)


################################
try:
    for dc in range(0,101,5):
        p.ChangeDutyCycle(dc)
        time.sleep(0.1)

    for dc in range(100,-1,-5):
        p.ChangeDutyCycle(dc)
        time.sleep(0.1)


except KeyboardInterrupt:
    pass
################################

p.stop()
GPIO.cleanup()
