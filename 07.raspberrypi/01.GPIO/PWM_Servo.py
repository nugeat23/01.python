import RPi.GPIO as GPIO
import time

servo_pin = 14

GPIO.setmode(GPIO.BCM)

GPIO.setup(servo_pin, GPIO.OUT)

p = GPIO.PWM(servo_pin,50)
p.start(0)

def move_angle(angle):
    dc = angle*0.055 + 2.5
    p.ChangeDutyCycle(dc)    
       


try:
    while True:
        # p.ChangeDutyCycle(7.5) # 90도
        # time.sleep(1)
        # p.ChangeDutyCycle(12.5) # 180도
        # time.sleep(1)
        # p.ChangeDutyCycle(2.5) # 0도
        # time.sleep(1)

        # 각도로 서보모터 제어하기
        # 각도 -> 듀티비 계산 후 ChangeDutyCycle() 호출

        move_angle(90)
        time.sleep(1)
        move_angle(180)
        time.sleep(1)
        move_angle(0)
        time.sleep(1)
        
except KeyboardInterrupt:
    pass


p.stop()
GPIO.cleanup()