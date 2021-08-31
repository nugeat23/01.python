import RPi.GPIO as GPIO
import time

btn = 26
green =19

GPIO.setmode(GPIO.BCM)

GPIO.setup(btn, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(green, GPIO.OUT)


light_on = False

def falling(channel):
    global light_on     #Global 변수선언
    if light_on ==False:
        GPIO.output(green,1)
        print("ON!")

    else:
        GPIO.output(green,0)
        print("OFF!")
    
    light_on = not light_on         # False <=> True


try:
    GPIO.add_event_detect(btn,GPIO.FALLING,callback=falling, bouncetime=300)
    while True:
        
        time.sleep(0.1)
        

except KeyboardInterrupt:
    pass

GPIO.cleanup()