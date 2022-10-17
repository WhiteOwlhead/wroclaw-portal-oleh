"main application configuration"

import os
# from dotenv import load_dotenv
from flask import *
import hashlib
from flask_cors import CORS
import sqlite3

# load_dotenv(dotenv_path="./.env.local")

DEBUG = bool(os.environ.get("DEBUG", True))

app = Flask(__name__)
CORS(app)

app.config["DEBUG"] = DEBUG


def getLoginDetails():
    # DATABASE NEEDS TO BE CREATED-users emails, passwords(they are hashed while registering so no problem)
    # plus their nicknames)
    with sqlite3.connect('database.db') as conn:
        cur = conn.cursor()
        if 'email' not in session:
            loggedIn = False
            nickname = ''
        else:
            loggedIn = True
            cur.execute("SELECT nickname FROM users WHERE email = '" + session['email'] + "'")
            nickname = cur.fetchone()
    conn.close()
    return (loggedIn, nickname)

@app.route("/")
def homePage():
    loggedIn, nickname = getLoginDetails()
    return render_template("home.html", loggedIn=loggedIn, nickname=nickname)
    # "function for initial testing"
    # return "Hello from Wroclaw Portal"


@app.route("/registerationForm")
def registrationForm():
    return render_template("register.html")

@app.route("/register", methods = ['GET', 'POST'])
def register():
    if request.method == 'POST':
        #Parse form data    
        
        email = request.form['email']
        password = request.form['password']
        passwordRepeated = request.form['passwordRepeated']
        nickname = request.form['nickname']

        with sqlite3.connect('database.db') as con:
            try:
                cur = con.cursor()
                cur.execute('INSERT INTO users (password, email, nickname) VALUES (?, ?, ?)', (hashlib.md5(password.encode()).hexdigest(), email, nickname))
                con.commit()
                msg = "Registered Successfully"
            except:
                con.rollback()
                msg = "Error occured"
        con.close()
        return render_template("login.html", error=msg)

@app.route("/loginForm")
def loginForm():
    if 'email' in session:
        return redirect(url_for('home'))
    else:
        return render_template('login.html', error='')

@app.route("/login", methods = ['POST', 'GET'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        if is_valid(email, password):
            session['email'] = email
            return redirect(url_for('home'))
        else:
            error = 'Invalid email / Password'
            return render_template('login.html', error=error)

@app.route("/logout")
def logout():
    session.pop('email', None)
    return redirect(url_for('home'))

def is_valid(email, password):
    con = sqlite3.connect('database.db')
    cur = con.cursor()
    cur.execute('SELECT email, password FROM users')
    data = cur.fetchall()
    for row in data:
        if row[0] == email and row[1] == hashlib.md5(password.encode()).hexdigest():
            return True
    return False

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
