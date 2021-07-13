class NameCard:
    def __init__(self, name, email, phone, address):
        self.name = name
        self.email = email
        self.phone = phone
        self.address = address

    def print(self):
        print(f"{self.name}, {self.email}, {self.phone},{self.address}")



n1 = NameCard('둘리','dooli@gmail.com','010-1111-3333','경기도 안양시')
# print(f"{n1.name}, {n1.email}, {n1.phone},{n1.address}")
print(n1.name)
print(n1.email)
n1.print()

book =[
    # 하드코딩(hard coding)
    # NameCard('둘리','dooli@gmail.com','010-1111-3333','경기도 안양시'),
    # NameCard('도우너','douner@naver.com','010-1111-4444','경기도 수원시'),
    # NameCard('홍길동', 'hong@gmail.com', '010-1111-1111', '서울시 강남구'),
    # NameCard('고길동', 'go@gmail.com', '010-1111-2222', '서울시 서초구'),
    # NameCard('마이콜', 'mickol@hanmail.net', '010-1111-1111', '인천광역시')

]


# addressbook.txt를 읽어서 NameCard의 리스트를 리턴하는 함수
def load(file_name):
    book = []
    with open(file_name,'rt',encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            line = line.split(',')      # 예:['둘리','email','000-000-0000','경기도 안양시']
            # nc = NameCard(line[0],line[1],line[2],line[3])
            nc = NameCard(*line)
            book.append(nc)
    return book

def print_book(book):
    for ix, nc in enumerate(book,1):
        print(f'{ix}) ', end='')
        nc.print()
        # print(f'{ix}) {nc.name}, {nc.email}, {nc.phone}, {nc.address}')
# book = load('C:/workspace/01.python/ch15/addressbook.txt')
book = load('addressbook.txt')

def orderby(nc):
    return nc.address

book.sort(key=orderby)  # book의 엘리먼트를 orderby 함수의 인자로 넘김

# book.sort(key = lambda nc: nc.address)
print_book(book)











