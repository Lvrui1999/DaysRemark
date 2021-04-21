import pymysql as sql
db = sql.connect("119.3.164.126","DB_USER47","DB_USER47@123","user47db" )
cursor = db.cursor()
cursor.execute('insert into user_password (uname,pword) values ("123","123")')
cursor.execute('select * from user_password where uname = "1"')
data = cursor.fetchone()
print (data)
db.close()
