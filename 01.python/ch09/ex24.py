# 좌표 3개를 가지는 리스트 데이터
locations = [(1,3),(2,4),(-1,20)]

for loc in locations:
    print(loc)
    print(f'x: {loc[0]}, y: {loc[1]}')

print()

for x, y in locations: #x, y = loc
    print(f'x: {x}, y: {y}')

result = divmod(7,3) # tuple을 리턴
print(result)

d, m = divmod(7,3)
print(d,m)


