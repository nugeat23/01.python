data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

data2 = [n*2 for n in data]

print(data2)

data3 = [n*10 for n in data if n%2==1]
print(data3)

scores = [80, 45, 76, 100, 66, 59, 99]
# 60점 미만의 성적만 추출
data4 = [s for s in scores if s < 60]
print(data4)

