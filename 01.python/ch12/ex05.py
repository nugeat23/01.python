import time

t = time.time()
print(t)
print(time.ctime(t))

now = time.localtime(t)

print(f"{now.tm_year}년 {now.tm_mon}월 {now.tm_mday}일")
print(f"{now.tm_hour}:{now.tm_min}:{now.tm_sec}")
