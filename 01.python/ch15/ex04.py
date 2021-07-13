import random
import time

class Sensor:
    def __init__(self,name,place):
        self.name = name    # 센서 이름
        self.place = place  # 설치 장소
        self.value = None   # 센서의 값
        
    def measure(self):
        self.value = random.randint(0,100) # 값을 임의로 배정, 값의 범위 0 ~ 100 사이의 정수
        return self.value

class Light:
    def __init__(self,place):
        self.place = place
        self.status = False # True: 켜짐, False: 꺼짐

    def on(self):
        self.status: True
        print(f'{self.place} 전등 켜짐')

    def off(self):
        self.status: False
        print(f'{self.place} 전등 꺼짐')





# temp = Sensor('온도','거실')
# humi = Sensor('습도','거실')

illu = Sensor('조도','거실')
light1 = Light('거실')

# 1초 간격으로 센서를 측정해서 출력하기
# 센서의 값이 40미만이면(어두워지면) 전등을 켜고,
# 센서의 값이 40이상이면(밝아지면) 전등을 끔.
while True:
    value = illu.measure()  # 센서 측정
    # print(f"{illu.name} : {value}")
    if value < 40 and light1.status == False:    # 전등이 꺼져 있으면
        light1.on()
    
    elif value >= 40 and light1.status == True:  # 전등이 켜져 있으면
        light1.off()

    time.sleep(1)   # 단위: 초

