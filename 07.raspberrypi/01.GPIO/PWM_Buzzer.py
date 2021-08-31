import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

GPIO.setup(6, GPIO.OUT)

p = GPIO.PWM(6,100)

Frq = [262,294,330,349,392,440,493,523]
speed = 0.5

p.start(10)

try:
    while True:
        for fr in Frq:
            p.ChangeFrequency(fr)
            time.sleep(speed)
            p.ChangeFrequency(10)
            time.sleep(0.1)

except KeyboardInterrupt:
    pass

p.stop()
GPIO.cleanup()