from flask import Flask, render_template, g
import sqlite3



app = Flask(__name__)
app.database = "sample.db"



@app.route("/")
def hello():
	g.db=connect_db()
	cur=g.db.execute('select * from posts')
	posts=[dict(title=row[0], description=row[1]) for row in cur.fetchall()]
	g.db.close()
	return render_template('index.html', posts=posts)

#connenct to database
def connect_db():
	return sqlite3.connect(app.database)

if __name__ == "__main__":
    app.run(debug=True)