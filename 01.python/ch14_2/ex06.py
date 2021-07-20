import sqlite3

con = sqlite3.connect('addr.db')
cursor = con.cursor()

sql = "delete from tbladdr where name ='김상형'"
cursor.execute(sql)
con.commit()

cursor.close()
con.close()