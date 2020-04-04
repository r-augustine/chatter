from flask import Flask, render_template, url_for
from wtform_fields import *
from passlib.hash import pbkdf2_sha256

from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
app.secret_key = 'replace later!'

db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(), nullable=False)


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():

    login_form = LoginForm()
    if login_form.validate_on_submit():
        return 'Great success'

    return render_template('login.html', form=login_form)


if __name__ == "__main__":
    app.run(debug=True)