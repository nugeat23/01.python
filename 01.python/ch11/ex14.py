list1 = ['a','b']
list2 = list1
list3 = list1.copy()    # 얕은 복사

print('list1 is list2', list1 is list2)

print('list1 is list3', list1 is list3)

print('list2 is list3', list2 is list3)

print('list1 == list3', list1 == list3)

