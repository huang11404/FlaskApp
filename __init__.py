from flask import Flask, render_template, g
import sqlite3
import pandas as pd
import numpy as np



app = Flask(__name__)
app.database = "sample.db"

#connenct to database
def connect_db():
	return sqlite3.connect(app.database)



@app.route("/")
def index():
	g.db=connect_db()
	cur=g.db.execute('SELECT * FROM ( SELECT * FROM taobao ORDER BY time  DESC LIMIT 240 )')
	taobao=[dict(time=row[0], m1=row[1], m2=row[2],m3=row[3],m4=row[4],m5=row[5],m6=row[6],m7=row[7],m8=row[8],m9=row[9], \
										 m10=row[10],m11=row[11],m12=row[12],m13=row[13],m14=row[14],m15=row[15],m16=row[16],m17=row[17], \
										 m18=row[18]) for row in cur.fetchall()]
	print taobao
	g.db.close()

	#for chart
	con = sqlite3.connect("sample.db")
	x = pd.read_sql_query("SELECT * FROM ( SELECT * FROM taobao ORDER BY time  DESC LIMIT 24 ) ORDER BY time  ASC", con)
	taobao_chart=x.values.T.tolist()
	
	for i, item in enumerate(taobao_chart[0]):
		taobao_chart[0][i]=int(item.split(' ')[1].split(':')[0])

	return render_template('index.html', posts=taobao, post_chart=taobao_chart,row=3)


@app.route("/<page>")
def information(page):
	
	return render_template('%s.html' % page )

@app.route("/daily_interest_rate")
def daily_interest_rate():
	#for table
	g.db=connect_db()
	cur=g.db.execute("SELECT * FROM ( SELECT * FROM taobao ORDER BY time  DESC LIMIT 240 )     where time like  '%00:00:0%';")
	taobao=[dict(time=row[0], m1=row[1], m2=row[2],m3=row[3],m4=row[4],m5=row[5],m6=row[6],m7=row[7],m8=row[8],m9=row[9], \
										 m10=row[10],m11=row[11],m12=row[12],m13=row[13],m14=row[14],m15=row[15],m16=row[16],m17=row[17], \
										 m18=row[18]) for row in cur.fetchall()]
	print taobao
	g.db.close()

	#for chart
	con = sqlite3.connect("sample.db")
	x = pd.read_sql_query("SELECT * FROM ( SELECT * FROM ( SELECT * FROM taobao ORDER BY time  DESC LIMIT 576 )     where time like  '%00:00:0%') ORDER BY time  ASC", con)
	taobao_chart=x.values.T.tolist()
	
	for i, item in enumerate(taobao_chart[0]):
		taobao_chart[0][i]=int(item.split(' ')[0].split('-')[2])

	return render_template('index.html', posts=taobao, post_chart=taobao_chart, row=3)


# @app.route('/test')
# def analysis():
# 	con = sqlite3.connect("sample.db")
# 	x = pd.read_sql_query("SELECT * FROM ( SELECT * FROM taobao ORDER BY time  DESC LIMIT 24 ) ORDER BY time  ASC", con)
# 	taobao_chart=x.values.T.tolist()
	
# 	for i, item in enumerate(taobao_chart[0]):
# 		taobao_chart[0][i]=int(item.split(' ')[1].split(':')[0])
# 	#print taobao[0]

# 	#print taobao
# 	#x = pd.DataFrame(np.random.randn(20, 5))
# 	return render_template("test.html", post_chart=taobao_chart)




if __name__ == "__main__":
	app.run(debug=True)