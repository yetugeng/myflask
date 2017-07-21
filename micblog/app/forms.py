# -*- coding:utf-8 -*-
from flask_wtf import Form #导入Form类
# 导入文本输入框，导入Boolean选择框，这个Boolean框就是打钩或者不打勾的功能
from wtforms import StringField, BooleanField, PasswordField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Email, Length


class LoginForm(Form):
    user_name = TextAreaField('user name', validators=[DataRequired(),Length(max=15)])
    remember_me = BooleanField('Remember_me', default=True)   #第二个remember_me是一个勾选框，告诉系统要不要勾选，默认不勾选
    submit = SubmitField('Log in')  # SubmitField() represents an ``<input type="submit">``.  This allows checking if a given submit button has been pressed.
                                    # 生成按钮，作用是submit，按钮显示的文本是Sign In


class SignUpForm(Form):
    user_name = StringField('user name',validators=[DataRequired(),Length(max=15)])
    user_email = StringField('user email',validators=[DataRequired(),Length(max=64)])
    submit = SubmitField('Sign up')

# Flask-WTF 模块
# http://docs.jinkan.org/docs/flask-wtf/install.html#id3
# 从 0.9.0 版本开始，Flask-WTF 不再从 WTforms 中导入任何东西，你需要从 WTForms 导入字段

# 为了能够处理 web 表单，我们将使用 Flask-WTF ，该扩展封装了 WTForms 并且恰当地集成进 Flask 中。
# 在 Flask-WTF 中，表单是表示成对象，Form 类的子类。一个表单子类简单地把表单的域定义成类的变量。
# OpenID 登录仅仅需要一个字符串，被称为 OpenID，这里user_name,remember_me...就是。
# 我们将在表单上提供一个 ‘remember_me’ 的选择框，以至于用户可以选择在他们的网页浏览器上种植 cookie ，当他们再次访问的时候，浏览器能够记住他们的登录。
