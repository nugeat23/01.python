# str = '89'
str = '89점'
try:
    score = int(str)
    print(score)
    a = str[5]

except Exception as err:
    print(err)

# except ValueError as err:
#     print(err)
#     print('점수의 형식이 잘못되었습니다.')
# except IndexError as err:
#     print(err)
#     print('첨자 범위를 벗어났습니다.')

# except (ValueError, IndexError):
#     print('점수의 형식이나 첨자가 잘못되었습니다.')


print('작업 완료')


