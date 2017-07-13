# -*- coding:utf-8 -*-
# 有__init__.py才能证明文件夹app1是个包，定义了包的属性和方法，当然也可以为空文件。
# 如果没有本文件的，则app1只是个文件夹，不具备包的特性。
# 当外部引用包app1时，就具备了如下初始化的环境：Flask，app2，views。
from flask import Flask
app = Flask(__name__)       #实例化了一个Flask，赋值给app2变量，该变量隶属app1包。
app.config.from_object('config')
from app import views    #引用了app1下面的views