# 1초에 5번 온도를 측정해서, 출력하는
# 시물레이션을 작성하세요.
import time
import random
ix = 1
try:

    while True:
        time.sleep(0.2)
        #온도 측정했다고 가정
        c = random.uniform(25, 30)
        print(f'{ix}번째 측정: {c:.2f}도')
        ix +=1

except KeyboardInterrupt:
    print('종료되었습니다.')
# print('*'*35)
# import calendar as cal
# print(cal.calendar(2021))
# print(cal.month(2024,1))