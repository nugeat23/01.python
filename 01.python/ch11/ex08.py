# 참조(주소) 변수
list1 = [1,2,3] # 주소를 복사
list2 = list1   # 주소를 복사

print(list1 ==list2)

list2[1] = 100
list1[2] = 200

print(list1)
print(list2)

print(list1 == list2)