dic = {
    'boy' : '소년',
    'school' : '학교',
    'book' : '책'

}

print(dic.get('boy'))
print(dic.get('get'))
print(dic.get('girl','사전에 없는 단어입니다.'))


# False로 해석되는 값: 0, None, '', [], ()
if dic.get('boy'):      # '소년' --> T, None --> F
    pass        # 사전에 있음.
else:
    pass        # 사전에 없음.


if 'student' in dic:
    print('사전에 있는 단어')
else:
    print('사전에 없는 단어')