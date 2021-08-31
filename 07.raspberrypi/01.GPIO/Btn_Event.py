import RPi.GPIO as GPIO
import time

def falling(channel):
    print(channel, "Button pushed!")

btn = 26

GPIO.setmode(GPIO.BCM)

GPIO.setup(btn, GPIO.IN, pull_up_down=GPIO.PUD_UP)



try:
    GPIO.add_event_detect(btn,GPIO.FALLING,callback=falling, bouncetime=300)
    while True:
        
        time.sleep(0.1)
        

except KeyboardInterrupt:
    pass

GPIO.cleanup()