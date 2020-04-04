from flask import Flask, render_template, url_for
from wtform_fields import *

app = Flask(__name__)
app.secret_key = 'replace later!'

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():

    login_form = LoginForm()
    if login_form.validate_on_submit():
        return 'you tried to login'

    return render_template('login.html', form=login_form)


if __name__ == "__main__":
    app.run(debug=True)