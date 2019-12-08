import os
from flask import Flask,session,render_template,request,redirect,url_for
from classes.cls import *

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL3")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)
app.secret_key = os.urandom(12)


@app.route("/")
def home():
    session['logged_in']= False
    session['username']=''
    session['password']=''
    return render_template('home.html')


@app.route("/login", methods = ['POST','GET'])
def login():
    if session.get('logged_in'):
        x=participants.query.all()
        return render_template('login.html',x=x)

    else:
        n=request.form.get('name')
        p=request.form.get("pass")
        u = users.query.filter_by(name = n).first()
        try:
            if(u.password == p):
                session['logged_in'] = True
                x=participants.query.all()
                return render_template('login.html',x=x)
            else:
                return render_template('error.html',msg ="invalid password")
        except:
            return render_template('error.html',msg ="invalid username")
    return redirect(url_for('home'))


@app.route('/add', methods = ['POST','GET'])
def add():
    if request.method =="GET":
        return redirect(url_for('login'))
