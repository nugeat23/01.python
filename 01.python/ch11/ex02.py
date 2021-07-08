dates = ['월','화','수','목','금','토','일']
food = ['갈비탕', '순대국', '칼국수', '삼겹살']

menu = zip(dates, food)

print(list(menu))
print()

menu = zip(dates, food)     #zip 1회용 시퀀스다.
for d,f in menu:
    print(f'{d}요일 메뉴: {f}')


menu = zip(dates, food) 
#print(list(enumerate(list(menu))))
# enumerate에 의한 엘리먼트의 모양
# (0, ('월', '갈비탕'))

for no, (d, f) in enumerate(menu,1):
    print(f'{no}){d}요일 메뉴: {f}')

menu = dict(zip(dates, food))
print(menu)
