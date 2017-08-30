from flask import render_template
from app import app
from app.LoginForm import LoginForm

@app.route("/login",methods=['GET','POST'])
def login():
    #接收参数
    form = LoginForm();
    print(form.username.data)
    name = form.username.data
    passwd = form.password.data
    if name == 'admin'and passwd == 'admin':
        print('username:'+form.username.data + 'and password:' + form.password.data)
        return render_template('index.html', form = form)
    return render_template('login.html', form = form)