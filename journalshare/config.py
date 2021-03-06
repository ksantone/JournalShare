import os

class Config:
	SECRET_KEY = '4296163e9874eb37e434a9d16ba2b63b'
	SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']
	MAIL_SERVER = 'smtp.gmail.com'
	MAIL_PORT = 587
	MAIL_USE_TLS = True
	MAIL_USERNAME = os.environ.get('EMAIL_USER')
	MAIL_PASSWORD = os.environ.get('EMAIL_PASS')

class ProductionConfig(Config):
	DEBUG = False