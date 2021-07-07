s = 'Good morning. my love KIM'

print(s.lower())
print(s.upper())
print(s.swapcase())
print(s.title())
print(s.capitalize())

# 원본에는 변화가 없음.
print(s)

# 문자열은 불변 개체다.

s = '   angel   '

print(s + '님')
print(s.strip()+'님')
print(s.lstrip()+'님')
print(s.rstrip()+'님')