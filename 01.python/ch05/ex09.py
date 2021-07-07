USER_ID = 'hong'
PASSWORD = 'abcd'

# 문제
# 사용자로 부터 id와 비밀번호를 입력받아
# userid, password 변수에 저장
# 로그인 가능 여부를 판정하고,
# 로그인 실패시 그 이유를 출력하세요.


for _ in range(3):
    userid = input('사용자 ID: ')
    password = input('비밀번호: ')
    print() # 빈 줄 출력

    if userid == USER_ID and password == PASSWORD:
        print('로그인 성공')
        print(userid, '님 반갑습니다.', sep='')
        break
    else:    # 로그인 실패
        print('로그인에 실패했습니다.')
        # #실패 이유 출력
        print('사용자 id 또는 비밀번호가 틀렸습니다.')
        # if userid != USER_ID:    #등록된 USER_ID가 아닌 경우
        #     print('등록된 사용자 ID가 아닙니다.')
        # elif password != PASSWORD:
        #     print('비밀번호가 다릅니다.')

# directory == folder
# CLI(Command Line Interface) --> directory
# GUI(Graphic User Interface) --> folder

