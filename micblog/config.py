# -*- coding:utf-8 -*-
import os
CSRF_ENABLED = True
SECRET_KEY = 'shi-yan-lou'

basedir = os.path.abspath(os.path.dirname(__file__))   #返回文件的绝对路径

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir,'app.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir,'db_repository')

# CSRF（Cross-site request forgery）跨站请求伪造，也被称为“One Click Attack”或者Session Riding，通常缩写为CSRF或者XSRF，是一种对网站的恶意利用。
