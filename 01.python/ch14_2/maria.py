import MySQLdb

db = MySQLdb.connect(host='localhost', user='iot', password='1234', db='employees')
con = db.cursor()

sql = 'select * from employees'
con.execute(sql)
table = con.fetchmany(10)

for record in table:
    print(record)

# 자원 해제 및 접속 해제
con.close()
db.close()