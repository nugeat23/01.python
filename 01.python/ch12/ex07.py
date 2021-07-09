import time

start = time.time()
for a in range(1000):
    print(a)

end =time.time()

print(end - start)

# 1 ~ 100000 까지의 합을 구하는데
# 소요된 시간을 출력하세요.

total = 0
start = time.time()
for num in range(1,100001):
    total += num
    
end =time.time()

print(end - start)
print(total)