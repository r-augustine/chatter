from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, Length, EqualTo

class LoginForm(FlaskForm):
    '''Login Form'''

    username = StringField('username', 
        validators=[InputRequired(
            message='Username required'),
            Length(min=4, max=25, message='Username must be between 4 and 25 characters')
        ])
    password = PasswordField('password_label',
        validators=[InputRequired(
            message='Username required'),
            Length(min=4, max=25, message='Username must be between 4 and 25 characters')
        ])
    submit_button = SubmitField('Sign In')