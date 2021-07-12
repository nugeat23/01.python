FILE_PATH = 'addressbook.txt' # 상수값이면 대문자로 쓰는 관례가 있음.

#  지정한 파일을 읽어서
#  다음 모양의 리스트를 반환하는 load_file을 작성하세요.
# [
#     [홍길동, hong@gmail.com, 010-1111-1111, 서울시 강남구]
#     [고길동, go@gmail.com, 010-1111-2222, 서울시 서초구]
#     [둘리, dooli@gmail.com, 010-1111-3333, 경기도 안양시]
#     [도우너, douner@naver.com, 010-1111-4444, 경기도 수원시]
#     [마이콜, mickol@hanmail.net, 010-1111-1111, 인천광역시]
# ]

def load_file(file_path):
    book = []
    # 파일을 읽어서 book 리스트 구성
    with open(file_path, 'rt', encoding='utf-8') as f:
        for line in f:
            line = line.strip() # 공백문자(' ', '\t','\n') 제거
            if not line:
                continue
            line = line.split(',')
            book.append(line)
    
    return book

# def orderby(x):
#     return x[1]     # email 파트

def save_book(file_path,book):
    with open(file_path,'wt',encoding='utf-8') as f:
        for item in book:
            # 리스트를 --> str
            line = ','.join(item)
            f.write(line+'\n')


try:
    book = load_file(FILE_PATH)
    # 이름으로 정렬해서 출력하세요.
    # book.sort()   # 이름으로 정렬
    # email로 정렬해서 출력하세요.
    # book.sort(key=orderby)  # email로 정렬
    book.sort(key=lambda x: x[3])   # 주소로 정렬
    for item in book:    
        print(item)

    # 정렬된 book을 파일에 다시 저장하세요.
    save_book(FILE_PATH,book)

except Exception as e:
    print('[에러]',e)