class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def intro(self):
        print(f'{self.age}살 {self.name}입니다.')


class Student(Human):
    def __init__(self, name, age, stunum):
        super().__init__(name, age)
        # Human.__init__(self, name, age)
        self.stunum = stunum

    def intro(self):    # override
        # super().intro()
        # print(f'학번: {self.stunum}')   # 후처리

        # print(f'{self.stunum}/{self.name})

        print(f'학번 {self.stunum}')    # 전처리
        super().intro()

    def study(self):
        print('python 상속을 학습 중')

kim = Human('김상형', 29)
kim.intro()

lee = Student('이승우',45,930011)
lee.intro()
lee.study()

