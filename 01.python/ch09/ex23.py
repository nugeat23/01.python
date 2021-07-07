# 튜플로 가능한 일
names = '이순신', '김유신', '강감찬'
lee, kim, kang = names # unpack

print(lee)
print(kim)
print(kang)

a, b = 12, 34
print(a, b)

a, b = b, a # swap
print(a, b)

values = [1,2,3]
a, b, c = values
print(a,b,c)

a = 10
b = 20
c = 30

d = (a, b, c)
print(d)

pos = (10, 20) # 좌표값
print(pos[0])  # x좌표
print(pos[1])  # y좌표

x, y = pos
print(x)
print(y)









