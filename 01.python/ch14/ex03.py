text=''
line = 1

try:
    with open('live.txt','rt', encoding='utf-8') as f:
        while True:
            row = f.readline()
            if not row: break # 파일의 끝이면 종료

            text += f'{line} : {row}'
            line += 1
except Exception as e:
    print('[에러]',e)

print(text)

