import os
from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail
app = Flask(__name__)

app.config['SECRET_KEY'] = 'd5cd54703b4d2ce7dcf66cd9f606796c'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)
bcrypt=Bcrypt()
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'
app.config.update(
MAIL_SERVER='smtp.gmail.com',
MAIL_PORT='587',
MAIL_USE_TLS=True,
MAIL_USERNAME='a01021033096@gmail.com',
MAIL_PASSWORD='wuwxnudkvwzavkci'
)
mail = Mail(app)

from flaskblog.users.routes import users
from flaskblog.posts.routes import posts
from flaskblog.main.routes import main
from flaskblog.errors.handlers import errors

app.register_blueprint(users)
app.register_blueprint(posts)
app.register_blueprint(main)
app.register_blueprint(errors)
