price = 1000

def sale():
    price = 500
    print('지역변수 price', price,id(price))

sale()
print('전역변수 price',price,id(price))

print('*'*35)

price = 1000

def sale():
    global price
    price = 500

sale()
print(price)



