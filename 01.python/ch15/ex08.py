class Car:
    count = 0

    @staticmethod
    def hello():
        print('오늘도 안전운행')
        
    def __init__(self,name):
        self.name = name
        self.serial = Car.count
        Car.count += 1

    @classmethod
    def outcount(cls):
        print(cls.count)

    def intro(self):
        print(f'{self.name} ({self.serial})')

Car.hello()

print(Car.count)

pride = Car('프라이드')
pride.intro()
korando = Car('코란도')
korando.intro()

Car.outcount()



# print(Car.count)
# Car.count = 100
# Car.outcount()
