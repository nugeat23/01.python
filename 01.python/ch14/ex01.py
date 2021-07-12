# 윈도우즈
file_path = '\\temp\\test_a\\live.txt'
# # mac
# file_path = 'data/live.text'


f = open(file_path, 'wt', encoding = 'utf-8')
f.write("""삶이 그대를...
슬퍼하거나 노하지 말라!.




:
끝\n""")
f.write('더 추가가능함...\n')
f.write('또 추가 가능함...')
f.close()
print('-'*30)
try:
    with open(file_path, 'wt', encoding = 'utf-8') as f:
        f.write("""삶이 그대를...
슬퍼하거나 노하지 말라!.




:
끝\n""")
        f.write('더 추가가능함...\n')
        f.write('또 추가 가능함...')
except Exception as e:
    print('[에러]', e)













