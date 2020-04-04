from flask import Flask, render_template, url_for, redirect
from wtform_fields import *
from passlib.hash import pbkdf2_sha256
from flask_login import LoginManager, UserMixin, login_user, current_user, logout_user, login_required

from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
app.secret_key = 'replace later!'

db = SQLAlchemy(app)

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(), nullable=False)


# Configure flask login
login = LoginManager(app)
login.init_app(app)

@login.user_loader
def load_user(id):
    return User.query.get(int(id))

@app.route('/', methods=['GET'])
def index():
    
    if current_user.is_authenticated:
        user = current_user.name
        return render_template('index.html', user=user)
    return redirect('/login')

@app.route('/login', methods=['GET', 'POST'])
def login():

    login_form = LoginForm()
    if login_form.validate_on_submit():
        user = User.query.filter_by(name=login_form.username.data).first()
        login_user(user)
        return redirect('/')

    return render_template('login.html', form=login_form)

@app.route('/chat', methods=['GET'])
@login_required
def chat():
    # if not current_user.is_authenticated:
    #     return 'Please login to view this page!'
    return 'this is chat route'

@app.route('/logout', methods=['GET'])
def logout():
    logout_user()
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)