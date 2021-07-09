def total(s,b):
    return s + b

score = [ 45,89,72,53,94 ]
bonus = [ 2,3,0,0,5 ]
for x in map(total, score, bonus):
    print(x, end = ' ,')

print()
country = ['Korea', 'America', 'Iran', 'France', 'North korea']
# 문자열의 첫글자로만 구성된 리스트를 만드세요.
# ['K', 'A', ...]

# datas = []
# for c in country:
#     datas.append(c[0])

# print(datas)
print()

def convert(s):
    return s[0]

datas = list(map(convert, country))
print(datas)
