f = open('live.txt', 'rt', encoding='utf-8')

f.seek(12, 0)       # 12 바이트가 문자 중간 위치에 있으므로
text = f.read()     # 예외 발생
f.close()

print(text)