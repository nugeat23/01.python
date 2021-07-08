def calcstep(begin, end, step):
    total = 0
    for num in range(begin, end+1, step):
        total += num
    
    return total

print(f'3 ~ 5 = {calcstep(3,5,1)}')
print(f'3 ~ 5 = {calcstep(begin=3,end=5,step=1)}')
print(f'3 ~ 5 = {calcstep(step=1,end=5,begin=3)}')
print(f'3 ~ 5 = {calcstep(3,5,step=1)}')
print(f'3 ~ 5 = {calcstep(3,end=5,step=1)}')
print(f'3 ~ 5 = {calcstep(end=3,begin=5,step=1)}')

# def calcstep2(begin, end=1, step):  
#     pass

# calcstep2(10,20) --> 두가지 해석 가능