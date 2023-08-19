# Check fixes in line 13

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__, static_folder='static', template_folder='templates')
app.config['SQLALCHEMY_DATABASE_URI']   = 'sqlite:///webdatabase.db'
app.config['SECRET_KEY'] = 'eea013094d828aeb51a619aa'
db=SQLAlchemy(app)

# Fix - Added line 13. This mainly fixed the error
app.app_context().push()

bcrypt=Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = "login_page"
login_manager.login_message_category="info"

from webfiles import routes