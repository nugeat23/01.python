def test():
    list1 = [1,2,3]
    print(list1)
    return list1

def test2(l2):
    l2[0] = 100
    print(l2)



l1 = test()
print(l1)

test2(l1)
print(l1)

