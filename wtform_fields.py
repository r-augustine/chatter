from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import InputRequired, Length, EqualTo

class LoginForm(FlaskForm):
    '''Login Form'''

    username = StringField('username')
    password = PasswordField('password_label')