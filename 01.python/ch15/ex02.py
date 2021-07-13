class Human:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def intro(self):
        print(f'{self.age}살 {self.name}입니다.')


kim = Human('김상형', 29)
kim.intro()

lee = Human('이승우',45)
lee.intro()

lee = kim
lee.intro()