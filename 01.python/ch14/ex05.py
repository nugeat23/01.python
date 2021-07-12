try:
    with open('live.txt','rt', encoding = 'utf-8') as f:
        for line in f:
            print(line, end="")

except Exception as e:
    print('[에러]',e)

