score = [88,95,70,100,99,88,78,50]
score.remove(100)
print(score)

del(score[2])
print(score)

score[1:4] = []
print(score)


print(50 in score)
print(-100 in score)
#print(score.find(100)) #list는 find함수가 없음.

if -100 in score:
    score.remove(-100)