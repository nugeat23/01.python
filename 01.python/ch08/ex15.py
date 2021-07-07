price = 500
# print('궁금하면 ' + price + '원') # 에러 발생
print('궁금하면 ' + str(price) + '원!')

month = 8
day = 15
anni = '광복절'
print('%d월 %d일은 %s이다.' %(month, day, anni))

#print('%d월 %d일은 %s이다.' %(month, day))    #에러

# 위의 기법은 파이썬 3.6 버전까지 쓰던 기법
# 파이썬 3.7부터 새로운 포맷팅 기법이 나왔음

print(f'{month}월 {day}일은 {anni}이다.')
print('{month}월 {day}일은 {anni}이다.')

message = f'{month}월 {day}일은 {anni}이다.'
print(message)

height = 12.123456
print(f'키 : {height}')
print(f'키 : {height:.2f}')
print(f'키 : {height:10.3f}')   #총 10자리, 소숫점 3자리

