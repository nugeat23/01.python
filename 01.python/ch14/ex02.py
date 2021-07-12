try:
    f = None
    f = open('live.txt', 'rt', encoding = 'utf-8')
    text = f.read()
    print(text)

except FileNotFoundError:
    print('파일이 없습니다.')


# except Exception as e:
#     print('파일이 없습니다.')
#     #print(e)

finally:
    if f :
        f.close()

print()
try:
    with open('live.txt', 'rt', encoding = 'utf-8') as f:
        text = f.read()
        print(text)
        # with 블럭이 끝났을 때 해당 객체(f)의 close()를 자동 호출
except Exception as e:
    print(e)

