# 파일목록
# 1) addressbook copy.txt
# 2) addressbook.txt
# 3) live.txt
# 4) live2.txt
# 5) memo.txt

# 파일 선택: 3
# live.txt 내용을 출력

# 파일 선택: -1
# 종료

# 무한루프로 운영
import os

# 디렉토리에서 지정한 파일 확장자를 가지는 파일 목록 얻기
def get_files(dir_path, ext):
    files = os.listdir(dir_path)
    return list(filter(lambda file: file.endswith(ext),files))

# 전달된 목록 출력
def print_file_list(files):
    print('파일목록')
    for ix, file in enumerate(files, 1):
        print(f'{ix}) {file}')

# 파일의 내용을 출력
def print_file(file_name):
    # print(file_name)
    try:
        with open(file_name, 'rt', encoding='utf-8') as f:
            text = f.read()
            print(text)

    except Exception as e:
        print('[에러]', e)

while True:
    files = get_files('.','.txt')
    print_file_list(files)
    sel_num = int(input('파일 선택: '))
    if sel_num == -1:   # 종료
        break   # sys.exit(0)
    else:
        print_file(files[sel_num-1])










