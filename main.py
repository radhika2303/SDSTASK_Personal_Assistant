#flask is a web farmework written in python helping create websites
from flask import Flask,render_template,request     #flask package

app=Flask(__name__) #creating app variable

@app.route('/') #creating decorator
def login():
    return render_template('login.html')

@app.route('/register')
def about():
    return render_template('register.html')

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/login_validation',methods=['POST'])
def login_validation():
    email=request.form.get('email')
    password=request.form.get('password')
    return "The email is {} and the password is {}".format(email,password)

if __name__=="__main__":
    app.run(debug=True) #debug=True is written so that we dont need to run again n again after making changes

