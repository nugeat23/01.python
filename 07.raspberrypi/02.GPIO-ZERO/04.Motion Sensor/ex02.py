from gpiozero import MotionSensor, LED
from signal import pause
from datetime import datetime

pir = MotionSensor(12)
led = LED(13)
start = 0

def start_record():
    led.on()
    # 카메라 녹화 시작
    # 년월일_시분초.avi 파일명 출력
    global start
    start = datetime.now()
    fname = start.strftime('%Y.%m.%d_%H:%M:%S.avi')     # %f: 밀리초
    print('녹화시작', fname)

def stop_record():
    led.off()
    # 카메라 녹화 중지
    end = datetime.now()
    delta = end - start                 # 시간에 대해서 빼기 연산 --> timedelta 타입
    print('녹화중지(녹화시간)', delta)




pir.when_motion = start_record
pir.when_no_motion = stop_record

pause()