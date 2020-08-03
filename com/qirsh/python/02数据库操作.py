from pymysql import *

conn = connect("localhost","root","","emp",3306)
cur = conn.cursor()
count = cur.execute("select * from emp")
print(count)
result = cur.fetchall()
for i in result:
    print(i)

conn.close()