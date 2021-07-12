import os

files = os.listdir('.')
cwd = os.getcwd()
print(cwd)


for f in files:
    # print(f)
    # # 절대경로로 출력
    fpath = os.path.join(cwd,f) # 경로 결합
    # print(f'{cwd}\\{f}')
    # 디렉토리인 경우 앞에 <dir>을 붙여서 출력
    if os.path.isdir(fpath):    # 디렉토리인 경우
        print(f'<dir> {fpath}')
    
    else:
        print(fpath)

# 지정한 확장명을 가지는 파일명 목록을 리턴하는
# get_files(dir_path, ext)

def get_files(dir_path, ext):
    files = os.listdir(dir_path)
    # 1. filter() 함수
    return list(filter(lambda file: file.endswith(ext),files))
        
    # 2. 컴프리핸션
    return [file for file in files if file.endswith(ext)]
    
    
    # 3. 일반 순회
    # result = []
    # for file in files:
    #     if file.endswith(ext):             # file의 확장명이 ext이면
    #         result.append(file)
    
    # return result

files = get_files('.','.txt')
print(files)








