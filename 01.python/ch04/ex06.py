# 문제 seconds 변수의 초 값을
# 분:초 로 출력하세요.

seconds = 3150
print(seconds//60, ':', seconds%60)

seconds = 3150
print(seconds//60, seconds%60, sep=':')
print('현재시간',seconds//60, seconds%60, sep=':')


ms = 123456789 #밀리초
# 1000밀리초 = 1초
# 시:분:초.밀리초

seconds = ms // 1000 #123456초
ms = ms % 1000 #789밀리초

print(seconds, ms)
hours = seconds // 3600 #시
minutes = (seconds%3600) //60 #분
print('현재시간 ',hours,':',minutes,':'
,seconds,'.',ms,sep='')



