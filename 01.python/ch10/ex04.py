# USER_ID = 'kim'
# PASSWORD = '1234'

users = {       # userid를 key로, password를 value로 하는 사전
    'kim' : '1234',
    'hong' : '12',
    'lee' : 'abc'

}

user_id = input('user_id: ')
password = input('password: ')

if (user_id in users) and (password == users[user_id]):
    print('로그인 성공')
else:
    print('로그인 실패')




# if user_id == USER_ID and password == PASSWORD:
#     pass
# else:
#     pass

