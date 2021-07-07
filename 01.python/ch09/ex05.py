lol =[
    [1,2,3],
    [4,5],
    [6,7,8]
]

print(lol)
print(lol[0])
print(lol[2][1])

# 순회: 콜렉션의 모든 데이터를 한 번씩 꺼내보는 것
print('-'*15)
for sub in lol:
    #print(sub)
    for item in sub:
        print(item, end=" ")
    print()



