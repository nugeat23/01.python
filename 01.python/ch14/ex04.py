try:
    with open('live.txt', 'rt', encoding='utf-8') as f:
        rows = f.readlines()
        
except Exception as e:
    print('[에러]', e)

for row in rows:
            print(row, end='')