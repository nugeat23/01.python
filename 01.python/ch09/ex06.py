score = [

[88,76,92,98],

[65,70,58,92],

[82,80,78,88]

]

total = 0       #전체 총점
totalsub = 0    #전체 과목 수

for student in score:
    subject_total = 0
    for subject in student:
        subject_total += subject
    subjects = len(student)
    average = subject_total/subjects
    print(f'학생 총점 {subject_total}, 평균 {average:.2f}')

    total += subject_total
    totalsub += subjects

average = total/totalsub
print(f'전체 평균 {average:.2f}')






