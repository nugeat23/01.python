import sqlite3

con = sqlite3.connect('addr.db')
cursor = con.cursor()

# 검색할 이름을 사용자로부터 입력받아서 처리
name = input('이름: ')
sql = f"select * from tbladdr where name = '{name}'"
cursor.execute(sql)

record = cursor.fetchone()  #Primary Key절로 구성한 경우 사용
if record:
    print(record)
else:
    print('데이터 없음')

cursor.close()
con.close()