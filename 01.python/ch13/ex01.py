# str = '89'    # 성공하는 경우

str = '89점'    # 실패하는 경우

try:
    score = int(str)
    print(score)

except:
    print('예외가 발생했습니다.')

print('작업완료 --> try문과 무관함.')