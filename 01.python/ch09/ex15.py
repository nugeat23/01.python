ans = input('결제 하시겠습니까?')

ans = ans.lower() #대문자를 소문자로 바꿔서 모두 인식

#YES, Yes, Ok, ok, ...
if ans in ['yes', 'y', 'ok', '예']:
    print('결제를 진행합니다.')

else:
    print('결제를 취소합니다.')



