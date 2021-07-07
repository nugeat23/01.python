dic ={
    'boy' : '소년',
    'school' : '학교',
    'book' : '책',

}

print(dic.keys())          #출력되는게 list 아님. dict_keys라는 collection
print(dic.values())        #순회는 되는데, 업데이트는 안됨.
print(dic.items())

# 순회: 루프를 통해서 콜렉션의 데이터를 모두 처리하는 것
# 사전 순회 방법 1: .keys()
keylist = dic.keys()
for key in keylist:
    print(key, dic[key])

print()

for key in dic.keys():
    print(key, dic[key])

# 사전 순회 방법 2: .items()
for item in dic.items():
    print(item, item[0], item[1] )

print()
for key, value in dic.items():  #unpac: key, value = (key, value)
    print(key, value)
print('-'*15)
# 사전 순회 방법 3
for _ in dic:
    print(_, dic[_])






