import random

food = ['짜장면', '짬뽕', '탕수육', '군만두']
print(random.choice(food))

print()

i = random.randrange(len(food))
print(food[i])

print()

print(random.sample(food,2))

print()

random.shuffle(food)
print(food)

print()

nums = random.sample(range(1,46), 6)
nums.sort()
print(nums)