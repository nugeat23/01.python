class NameCard:
    def __init__(self, name, email, phone, address):
        self.name = name
        self.email = email
        self.phone = phone
        self.address = address

    def print(self):
        print(f"{self.name}, {self.email}, {self.phone},{self.address}")


class AddressBook:
    def __init__(self):
        self.book = []
    
    def load(self, file_name):
        self.book = []
        with open(file_name,'rt',encoding='utf-8') as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                line = line.split(',')      # 예:['둘리','email','000-000-0000','경기도 안양시']
                # nc = NameCard(line[0],line[1],line[2],line[3])
                nc = NameCard(*line)
                self.book.append(nc)

    def save(self, file_name):
        with open(file_name,'wt',encoding='utf-8') as f:
            for nc in self.book:
                line = f'{nc.name},{nc.email},{nc.phone},{nc.address}'
                f.write(line + '\n')

    # 사용자로부터 이름, email, phone, 주소 정보를 입력받고,
    # book에 추가하는 메서드
    def add(self):
        name = input('이름: ')
        email = input('email: ')
        phone = input('전화번호: ')
        address = input('주소: ')

        nc = NameCard(name, email, phone, address)
        self.book.append(nc)
        self.sort   # 자기 자신의 다른 메서드를 호출하는 것

    def find(self):
        name = input('검색할 이름: ')
        for nc in self.book:
            if name == nc.name:
                nc.print()
                return

        # 루프가 끝나면 찾지 못한 것
        print(f'{name}은 주소록에 없습니다.')
    

    def print(self):
        for ix, nc in enumerate(self.book,1):
            print(f'{ix}) ', end='')
            nc.print()

    def sort(self):
        self.book.sort(key=lambda nc:nc.name)


book = AddressBook()

# 데이터 로드
book.load('addressbook.txt')


# book.print()
# # 정렬 후 저장
# book.sort()
# book.print()
# book.save('addressbook2.txt')

# # 데이터 추가 & 저장
# book.add()
# book.print()
# book.save('addressbook3.txt')

book.find()






