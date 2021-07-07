score = [88,95,70,100,99]
sorted_score = sorted(score)

print(score)
print(sorted_score)

score = [88,95,70,100,99]
sorted_score = sorted(score, reverse=True)

print(score)
print(sorted_score)


# [88,95,70,100,99,88,78,50]

# 검색 값: 79
# [50,70,78,88,88,95,99,100]
# [50,70,78,88]
# [78,88]
# [78]

# 검색 값: 99
# [50,70,78,88,88,95,99,100]
# [95,99,100]
