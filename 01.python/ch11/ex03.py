def flunk(s):
    return s < 60

score = [45,89,72,53,94]
for s in filter(flunk,score):
    print(s)


print(flunk(95))
a = flunk
print(a(95))
print(id(a), id(flunk))


prn = print     # print 함수 코드 1벌인데, 사용할 수 있는 이름 2개가 됨.
prn(1,2,3, '출력')
print(id(prn), id(print))

