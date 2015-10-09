import urllib2
import re
from bs4 import BeautifulSoup

from datetime import datetime
import pytz
import sqlite3

def insert_sqlite(time, m7, m8, m9, m10, m11, m12, m13, m14,  m15, m16, m17, m18, m19, m20, m21, m22, m23, m24):
	# create a new database if the database doesn't already exist
	with sqlite3.connect('../sample.db') as connection:

	    # get a cursor object used to execute SQL commands
		c = connection.cursor()

	    # create the table
		c.execute('CREATE TABLE IF NOT EXISTS taobao(time TEXT, m7  REAL, m8 REAL, m9 REAL, m10 REAL, m11 REAL, m12 REAL, m13 REAL, \
																m14 REAL, m15 REAL, m16 REAL, m17 REAL, m18 REAL, m19 REAL, m20 REAL, \
																m21 REAL, m22 REAL, m23 REAL, m24 REAL)')

	    # insert dummy data into the table
		c.execute('INSERT INTO taobao VALUES(?, ?, ?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)', (time, m7, m8, m9, m10, m11, m12, m13, m14, \
																							   m15, m16, m17, m18, m19, m20, m21, m22, m23, m24))
	    #c.execute('INSERT INTO taobao VALUES("Well", "I\'m well.")')
	    #c.execute('INSERT INTO taobao VALUES("Excellent", "I\'m excellent.")')
	    #c.execute('INSERT INTO taobao VALUES("Okay", "I\'m okay.")')


# get date
current_time = datetime.now(pytz.timezone('Asia/Shanghai'))
print(current_time.strftime('%Y-%m-%d %H:%M:%S %Z%z'))
current_time=current_time.strftime('%Y-%m-%d %H:%M:%S %Z%z')



interest=[]
for minmonth in range(7,25):

	if minmonth==24:
		maxmonth=9999
	else:
		maxmonth=minmonth+1
	print str(minmonth)+str(maxmonth)


	#grap interest
	opener= urllib2.build_opener()
	opener.addheaders=[('User-agent', 'Mozilla/5.0')]


	url=('https://zhaocaibao.alipay.com/pf/productQuery.htm?pageNum=1&minMonth='+str(minmonth)+'&maxMonth='+str(maxmonth)+'&minAmount=&danbao=1')

	ourUrl= opener.open(url).read()

	soup= BeautifulSoup(ourUrl)

	#title=soup.title.text

	body=soup.find('span', class_='f-18')

	text=re.findall(r'\d+.\d+', body.text)

	
	#outfile=open('../wikipedia.txt', 'a')
	#outfile.write(current_time+'    month:'+str(minmonth)+'    interest:'+str(text)+'\n')
	interest.append(float(text[0]))

#print interest[0],interest[1],interest[2],interest[3],interest[4],interest[5]


print current_time,interest[0],interest[1],interest[2],interest[3],interest[4],interest[5] ,interest[6],interest[7],interest[8],interest[9],interest[10],interest[11] ,interest[12],interest[13],interest[14],interest[15],interest[16],interest[17] 
insert_sqlite(current_time,interest[0],interest[1],interest[2],interest[3],interest[4],interest[5] ,interest[6],interest[7],interest[8],interest[9],interest[10],interest[11] ,interest[12],interest[13],interest[14],interest[15],interest[16],interest[17] )