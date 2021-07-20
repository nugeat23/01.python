import sqlite3

con = sqlite3.connect('addr.db')
cursor = con.cursor()

sql = 'select * from tbladdr order by addr'
cursor.execute(sql)

# select문 결과 전체 리턴
# cursor에서 결과 얻기 fetchall(), fetchmany(n), fetchone()
# table = cursor.fetchall()   # 전체 행이 담긴 list를 리턴, 행이 없으면 []
table = cursor.fetchmany(2)

for record in table:
    print(f'이름: {record[0]}, 전화: {record[1]}, 주소: {record[2]}')

# print(type(table))
# print(table)

print()
table = cursor.fetchmany(2)
for record in table:
    print(f'이름: {record[0]}, 전화: {record[1]}, 주소: {record[2]}')

print()
table = cursor.fetchmany(2)
for record in table:
    print(f'이름: {record[0]}, 전화: {record[1]}, 주소: {record[2]}')


cursor.close()
con.close()