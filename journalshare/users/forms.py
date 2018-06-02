from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from flask_login import current_user
from journalshare.models import User

class RegistrationForm(FlaskForm):
	username = StringField('Username',
		validators=[DataRequired(), Length(min=6, max=20)])
	email = StringField('Email',
		validators=[DataRequired(), Email()])
	password = PasswordField('Password',
		validators=[DataRequired(), Length(min=6, max=20)])
	confirm_password = PasswordField('Confirm Password',
		validators=[DataRequired(), EqualTo('password')])
	submit = SubmitField('Sign Up')

	def validate_username(self, username):
		user = User.query.filter_by(username=username.data).first()
		if user:
			raise ValidationError('The username you have entered is already taken.')

	def validate_email(self, email):
		user = User.query.filter_by(email=email.data).first()
		if user:
			raise ValidationError('The email you have entered is already taken.')

class LoginForm(FlaskForm):
	username = StringField('Username',
		validators=[DataRequired()])
	password = PasswordField('Password',
		validators=[DataRequired()])
	remember = BooleanField('Remember Me')
	submit = SubmitField('Login')

class UpdateAccountForm(FlaskForm):
	username = StringField('Username',
		validators=[DataRequired(), Length(min=6, max=20)])
	email = StringField('Email',
		validators=[DataRequired(), Email()])
	picture = FileField('Update Profile Picture', validators=[FileAllowed(['jpg', 'png'])])
	submit = SubmitField('Update')

	def validate_username(self, username):
		if username.data != current_user.username:
			user = User.query.filter_by(username=username.data).first()
			if user:
				raise ValidationError('The username you have entered is already taken.')

	def validate_email(self, email):
		if email.data != current_user.email:
			user = User.query.filter_by(email=email.data).first()
			if user:
				raise ValidationError('The email you have entered is already taken.')

class RequestResetForm(FlaskForm):
	username = StringField('Username',
		validators=[DataRequired()])
	submit = SubmitField('Request Password Reset')

	def validate_username(self, username):
		user = User.query.filter_by(username=username.data).first()
		if user is None:
			raise ValidationError('There is no account with that username.')

class ResetPasswordForm(FlaskForm):
	password = PasswordField('Password',
		validators=[DataRequired()])
	confirm_password = PasswordField('Confirm Password',
		validators=[DataRequired(), EqualTo('password')])
	submit = SubmitField('Reset Password')