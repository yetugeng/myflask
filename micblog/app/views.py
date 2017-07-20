#-*- coding:utf-8 -*-
# from app import app
# from flask import render_template,flash,redirect
# from forms import LoginForm

import datetime

from flask import render_template,flash,redirect,sessions,url_for,request,g
from flask.ext.login import login_user,logout_user,current_user,login_required

from models import  User,Post,ROLE_USER,ROLE_ADMIN
from app import app,db,lm
from forms import  LoginForm,SignUpForm

@lm.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route('/')
@app.route('/index')
def index():
    user = { 'nickname':'yetugeng','nickname2':'gengxianren'}  # 用户名
    posts = [ # 提交内容
        {
            'author':{ 'nickname':'Johon'},
            'body':'Beautiful day in Portland!'
        },
        {
            'author':{ 'nickname':'susan'},
            'body':'The Avengers movies was so cool!'
        }
    ]
    return render_template("index.html",title = 'Home',user = user, posts = posts)



@app.route('/login',methods = ['GET','POST'])
def login():
    # 验证用户是否被验证
    if current_user.is_authenticated:
        return redirect('index')
    # 注册验证
    form = LoginForm()
    if form.validate_on_submit():
        user = User.login_check(request.form.get('user_name'))
        if user:
            login_user(user)
            user.last_seen = datetime.datetime.now()

            try:
                db.session.add(user)
                db.session.commit()
            except:
                flash("The Database error!")
                return redirect('/login')
            flash('Your name:' + request.form.get('user_name'))
            flash('remember me?' + str(request.form.get('remember_me')))
            return redirect(url_for("users", user_id=current_user.id))
        else:
            flash('Login failed,Your name is not exist!')
            return redirect('/login')
    return render_template("login.html",title="Sign In",form=form)

    # # 导入 LoginForm 类,从这个类实例化一个对象，接着把它传入到模板中。这就是我们渲染表单所要做的。
    # form = LoginForm()
    # if form.validate_on_submit():
    #     flash('Login requested for Name: ' + form.name.data)
    #     flash('passwd: '+ str(form.password.data))
    #     flash('remember_me: ' + str(form.remember_me.data))
    #     return rediect('/index')
    # return render_template('login.html',title = 'Sign In',form = form)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/sign-up',methods=['GET','POST'])
def sign_up():
    form = SignUpForm()
    user User()
    if form.validate_on_submit():
        user_name = request.form.get('user_name')
        user_email = request.form.get('user_email')

        register_check = User.query.filter(db.or_(User.nickname == user_name,User.email == user_email)).first()\
        if register_check:
            flash("error: The user's name or email already exists!")
            return  redirect('/sign-up')

        if len(user_name) and len(user_email)
            user.nickname = user_name
            user.email = user_email
            user.role = ROLE_USER
            try:
                db.session.add(user)
                db.session.commit()
            except:
                flash("The Database error")
                return redirect(('/sign-up'))

            flash("Sign up Successful!")
            return redirect('/index')

    return render_template("sign_up.html,form=form")
