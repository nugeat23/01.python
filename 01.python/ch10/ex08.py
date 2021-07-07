dic ={
    'boy' : '소년',
    'school' : '학교',
    'book' : '책',

}

dic2 ={
    'student' : '학생',
    'teacher' : '선생님',
    'book' : '서적'

}

# dic.update(dic2)
# print(dic)

# # print(dic+dic2) # 에러

# dic, dic2 원본 유지
# 새로운 사전으로 dic, dic2를 merge하세요.
l1 = []     # 비어 있는 리스트

dic3 = {}   # 비어 있는 사전
dic3.update(dic)
dic3.update(dic2)

print(dic)
print(dic2)
print(dic3)

print()













