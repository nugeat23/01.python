def calcsum(n):
    if n < 0:
        raise ValueError('음수는 처리 불가')

    total = 0
    for i in range(n+1):
        total + i

    return total



try:
    print('~5=', calcsum(-5))

except Exception as e:
    print('입력값이 잘못되었습니다.')
    print(e)