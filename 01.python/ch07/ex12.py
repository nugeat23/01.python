def fn1():
    temp =1
    print('fn1 start', temp)
    fn2()   ####
    print('fn1 end', temp)

def fn2():
    temp = 'hello'
    print('fn2 start', temp)
    fn3()   ####
    print('fn2 end', temp)

def fn3():
    temp = [1,2,3]
    print('fn3 start', temp)
    print('fn3 end', temp)


fn1()
print('*'*20)
fn2()
print('*'*20)
fn3()
print('*'*20)
