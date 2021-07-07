score = [88,95,70,100,99,88,78,50]

print(f'학생수는 {len(score)}입니다.')
print(f'최고 점수는 {max(score)}입니다.')
print(f'최소 점수는 {min(score)}입니다.')

#print(f'최고 점수 학생은 {score.index(100)}번 째입니다')

max_value = max(score)
max_ix = score.index(max_value)
print(f'최고 점수는 {max_value}, 인덱스는 {max_ix}')

min_value = min(score)
min_ix = score.index(min_value)
print(f'최고 점수는 {min_value}, 인덱스는 {min_ix}')





