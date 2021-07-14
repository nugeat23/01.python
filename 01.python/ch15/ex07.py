class Date:
    # def __init__(self): # 디폴트 생성자(매개변수가 없는 생성자)
    #     pass
    
    def __init__(self, month):
        self.inner_month = month
    
    def getmonth(self):
        return self.inner_month

  
    def setmonth(self, month):
        if 1 <= month <= 12:
            self.inner_month = month
        
        # else:
        #     # 강제로 예외 발생
        #     raise Exception(f'1~12 범위의 값이어야 함 ({month})')

    month = property(getmonth, setmonth)

today = Date(8)
today.month = 15        # setter 호출
print(today.month)      # getter 호출

today.month = 9        # setter 호출
print(today.month)      # getter 호출