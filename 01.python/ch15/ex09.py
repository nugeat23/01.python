class Human:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def intro(self):
        print(f'{self.age}살 {self.name}입니다.')

    def __str__(self):      # override
        return f'<Human name: {self.name}, age: {self.age}>'

    def __repr__(self):     # override
        return f'<Human name: {self.name}>'

kim = Human('김상형', 29)
kim.intro()

lee = Human('이승우',45)
lee.intro()

print(lee)  # 해당 객체의 __str__() 호출
print(kim)

li = [kim, lee] # 해당 객체의 __repr__() 호출
print(li)






