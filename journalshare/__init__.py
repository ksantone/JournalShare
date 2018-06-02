from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail
from journalshare.config import Config

db = SQLAlchemy()
bcrypt = Bcrypt()
login_manager = LoginManager()
login_manager.login_view = 'users.login'
login_manager.login_message_category = 'info'
mail = Mail()

def create_app(config_class=Config):
	app = Flask(__name__)
	app.config.from_object(Config)

	with app.app_context():
		db.init_app(app)
	bcrypt.init_app(app)
	login_manager.init_app(app)
	mail.init_app(app)

	from journalshare.users.routes import users
	from journalshare.journals.routes import journals
	from journalshare.main.routes import main
	from journalshare.errors.handlers import errors
	app.register_blueprint(users)
	app.register_blueprint(journals)
	app.register_blueprint(main)
	app.register_blueprint(errors)

	return app