from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_migrate import Migrate
from .config import Config
from flask_admin import Admin

app=Flask(__name__)
app.config.from_object(Config)
db=SQLAlchemy(app)
# 初始化 migrate
# 两个参数一个是 Flask 的 app，一个是数据库 db
migrate=Migrate(app,db)
login_manager=LoginManager(app)
admin=Admin(app)

from . import views

