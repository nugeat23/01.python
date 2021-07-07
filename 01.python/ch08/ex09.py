
# while True:                   # 무한루프

for _ in range(3):              # 3회 반복11
    height = input('키 : ')
    if height.isnumeric():
        height = int(height)
        print('키 = ', height)
        break
    else:
        print('숫자만 입력하세요.')


