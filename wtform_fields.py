from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, Length, ValidationError
from app import User

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
            Length(min=4, max=25, message='Username must be between 4 and 25 characters'),
            
        ])
    submit_button = SubmitField('Sign In')

    def validate_password(self, password):
        ''' Username and password validation '''

        username = self.username.data
        password = password.data

        # Check if username is valid
        user = User.query.filter_by(name=username).first()
        if user == None:
            raise ValidationError('Username or password is incorrect')
        elif password != user.password:
            raise ValidationError('Username or password is incorrect')