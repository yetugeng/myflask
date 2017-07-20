# -*- coding:utf-8 -*-
from flask_wtf import Form
from wtforms  import TextField,BooleanField,PasswordField,SubmitField,TextAreaField
from wtforms.validators import  Required,Email,Length


class LoginForm(Form):
    user_name = TextAreaField('user name',validators=[Required(),Length(max=15)])
    remember_me = BooleanField('Remember_me', default=False)
    sbumit = SubmitField('Log in')

class SignUpForm(Form)
    user_name = TextField('user name',validators=[Required(),Length(max=15)])
    user_email = TextField('user email',validators=[Required(),Length(max=15)])
    submit = SubmitField('Sign up')

# Flask-WTF 模块
# http://docs.jinkan.org/docs/flask-wtf/install.html#id3
# 从 0.9.0 版本开始，Flask-WTF 不再从 WTforms 中导入任何东西，你需要从 WTForms 导入字段