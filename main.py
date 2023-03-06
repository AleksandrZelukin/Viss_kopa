from flask import Flask, request, render_template, redirect
from werkzeug.security import generate_password_hash, check_password_hash
import sqlite3

app = Flask(__name__)
app.secret_key = "111"
db = sqlite3.connect('login_password.db')
cursor = db.cursor()

sql_create = ('''CREATE TABLE IF NOT EXISTS users(
login TEXT,
password TEXT);''')

cursor.execute(sql_create)
db.commit()

@app.route('/')
def index():
  return render_template("index.html")


@app.route('/signup', methods=['GET', 'POST'])
def signup():
  if request.method == 'POST':
    login = request.form.get('login')
    password = request.form.get('password')
    password = generate_password_hash(password,method='sha256')
    newUser=[login,password]
    db = sqlite3.connect('login_password.db')
    cursor = db.cursor()
    cursor.execute('''INSERT INTO users VALUES(?,?)''',newUser)
    cursor.close()
    db.commit()
    db.close()
  return render_template('signup.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
  if request.method == 'POST':
    login = request.form.get('login')
    password = request.form.get('password')
    if password and check_password_hash(password):
      True
      db = sqlite3.connect('login_password.db')
      cursor = db.cursor()
      cursor.execute(('''SELECT password FROM users WHERE login = '{}';''').format(login))
      pas = cursor.fetchall()
      cursor.close()
       
      db.close()
  return render_template('login.html')

  
if __name__ == "__main__":
    app.run(host='127.0.0.1',debug=True)

