s = '짜장   짬뽕   탕수육'

menu = s.split()
print(menu)      #['짜장', '짬뽕', '탕수육']
print(type(menu))

s2 = '서울->대전->대구->부산'
cities = s2.split("->")
print(cities)

for city in cities:
    print(city)


file_path = '\\temp\\test_a\\a.txt'
print(file_path)

# spilt()을 사용해서 파일명 추출
file_name = file_path.split("\\")[-1]  #--> [temp, test_a, a.txt]
print(file_name)                #indxeing

dirs = file_name = file_path.split("\\")[:-1]  # slicing
print(dirs)    # ['', 'temp', 'test_a']

dir_path = '\\'.join(dirs)
print(dir_path)

s = '\\'
dir_path = s.join(dirs)
print(dir_path)


# 온도, 습도, 조도
data = '10, 60.4, 700'
datas = data.split(',')
print(datas)



# file_path에서 파일의 확장명을 추출하세요.
file_ext = file_path.split(".")[-1]
print(file_ext)

s3 = '백반'
menu2 = s3.split()
print(menu2)


