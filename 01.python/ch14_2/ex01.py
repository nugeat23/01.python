import sqlite3

# 커넥션(세션) 생성
con = sqlite3.connect('addr.db')
cursor = con.cursor()

# 여기서 SQL 명령을 실행
cursor.execute('DROP TABLE IF EXISTS tblAddr')

cursor.execute("""
CREATE TABLE tblAddr(
    name CHAR(16) PRIMARY KEY,
    phone CHAR(16),
    addr TEXT
)
""")

cursor.execute("INSERT INTO tblAddr VALUES('김상형', '123-4567', '오산')")
cursor.execute("INSERT INTO tblAddr VALUES('한경은', '555-1004', '수원')")
cursor.execute("INSERT INTO tblAddr VALUES('한주완', '444-1092', '대전')")

# commit() 호출 전에는 실제 데이터는 임시 메모리에서 처리되고 있음.
# commit()을 호출하면 변경된 부분을 실제 db에 기록
# caching 기법에 해당
con.commit()     

cursor.close()
con.close()