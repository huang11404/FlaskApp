

import sqlite3




with sqlite3.connect('../sample.db') as connection:

    # get a cursor object used to execute SQL commands
	c = connection.cursor()

    # create the table
	c.execute('SELECT * FROM ( SELECT * FROM taobao ORDER BY time  DESC LIMIT 3 ) ')

	taobao=[dict(time=row[0], m1=row[1], m2=row[2],m3=row[3],m4=row[4],m5=row[5],m6=row[6],m7=row[7],m8=row[8],m9=row[9], \
										 m10=row[10],m11=row[11],m12=row[12],m13=row[13],m14=row[14],m15=row[15],m16=row[16],m17=row[17], \
										 m18=row[18]) for row in c.fetchall()]

	print taobao

