race = ['저그','테란','프로토스']

print(list(enumerate(race)))

for x in enumerate(race):
    print(x[0], x[1])

print()

for ix, r in enumerate(race):
    print (ix+1,r)

print()

for ix, r in enumerate(race, 1):
    print (ix,r)

print('*'*35)

score = [88,95,70,100,99]

for no, s in enumerate(score,1):
    print(str(no) + '번 학생의 성적 :' , s)