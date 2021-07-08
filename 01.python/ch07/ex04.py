# def intsum(*ints):
# def intsum(*ints, weight):

def intsum(weight, *ints):
    print(type(ints))
    print(ints)
    
    total = 0
    for num in ints:
        total += num*weight
    
    return total

print(intsum(0.1,1,2,3))
print(intsum(0.3,5,7,9,11,13))
print(intsum(0.5,8,9,6,2,9,7,5,8))
print(intsum(1))

