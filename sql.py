# sql.py - Create a SQLite3 table and populate it with data


import sqlite3



def insert_sqlite(time, month, interest):
	# create a new database if the database doesn't already exist
	with sqlite3.connect('sample.db') as connection:

	    # get a cursor object used to execute SQL commands
	    c = connection.cursor()

	    # create the table
	    c.execute('CREATE TABLE IF NOT EXISTS taobao(time TEXT, month TEXT, interest TEXT)')

	    # insert dummy data into the table
	    c.execute('INSERT INTO taobao VALUES(?, ?, ?)', (time, month, interest))
	    #c.execute('INSERT INTO taobao VALUES("Well", "I\'m well.")')
	    #c.execute('INSERT INTO taobao VALUES("Excellent", "I\'m excellent.")')
	    #c.execute('INSERT INTO taobao VALUES("Okay", "I\'m okay.")')

if __name__ == "__main__":

	time='19:00'
	month='24'
	interest='6.5'

	insert_sqlite(time , month, interest)