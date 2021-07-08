salerate = 0.9

def kim():
    print('오늘의 할인율 :', salerate)

def lee():
    price = 1000
    print('가격 :', price*salerate)


kim()
salerate = 1.1
lee()

# 소문자로 user_id를 받아주는 함수
def get_userid():
    user_id = input('사용자 id: ')
    return user_id.lower()

user_id = get_userid()
print(user_id)