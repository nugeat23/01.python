country = ['Korea', 'America', 'Iran', 'France', 'North korea']

country.sort(key=str.lower)
print(country)


# 문자열의 길이로 정렬하세요.
# 길이가 짧은 문자열이 앞에 나오도록 함.

country.sort(key=len)
print(country)

