dic ={
    'boy' : '소년',
    'school' : '학교',
    'book' : '책',

}

# 문제
# dic의 내용을 key의 사전순으로
# 출력하세요.
#
# key 목록 추출
keys = list(dic.keys())
# keys = dic.keys() #dict_keys를 리턴, .sort() 할 수 없음.

# key 목록을 정렬
keys.sort()

# keys = sorted(dic.keys())

# ket 목록을 순회해서 사전을 출력
for key in keys:
    print(key, dic[key])

print('-'*15)
# for x in dic:
#     x = sorted[x]
#     print(x, dic[x])
# 키는 받아주지만 정렬이 되어있지않아서 문제해결이 안됨.

print(list(dic)) #key를 엘리먼트로 하는 리스트로 변환
# list(dic)
# list(dic.keys()) # 가독성이 좋음. 



















