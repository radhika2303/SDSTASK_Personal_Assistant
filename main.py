#flask is a web farmework written in python helping create websites
from flask import Flask,render_template,request,redirect,session    #flask package
import mysql.connector
import os

app=Flask(__name__) #creating app variable
app.secret_key=os.urandom(24)

conn=mysql.connector.connect(host="localhost",user="root",password="",database="mydb")
cursor=conn.cursor()


@app.route('/') #creating decorator
def login():
    return render_template('login.html')

@app.route('/register')
def about():
    return render_template('register.html')

@app.route('/home')
def home():
    if 'user_id' in session:
        return render_template('home.html')
    else:
        return redirect('/')

@app.route('/help')
def help():
    return render_template('help.html')

@app.route('/profile')
def profile():
    return render_template('profile.html')

@app.route('/birthday')
def birthday():
    return render_template('birthday.html')

@app.route('/todo')
def todo():
    return render_template('index.html')


@app.route('/login_validation',methods=['POST'])
def login_validation():
    email=request.form.get('email')
    password=request.form.get('password')

    cursor.execute("""SELECT * FROM `users` WHERE `email` LIKE '{}' AND `password` LIKE '{}'""".format(email,password))
    users=cursor.fetchall()
    if len(users)>0:
        session['user_id']=users[0][0]
        return redirect('/home')
    else:
        return redirect('/')
@app.route('/add_user', methods=['POST'])
def add_user():
    name=request.form.get('uname')
    email=request.form.get('uemail')
    password=request.form.get('upassword')

    cursor.execute("""INSERT INTO `users` (`user_id`,`name`,`email`,`password`) VALUES (NULL,'{}','{}','{}')""".format(name,email,password))
    conn.commit()

    cursor.execute("""SELECT * FROM `users` WHERE `email` LIKE '{}'""".format(email))
    myuser=cursor.fetchall()
    session['user_id'] = myuser[0][0]
    return redirect('/home')

@app.route('/logout')
def logout():
    session.pop('user_id')
    return redirect('/')

if __name__=="__main__":
    app.run(debug=True) #debug=True is written so that we dont need to run again n again after making changes



