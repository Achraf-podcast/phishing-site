from flask import Flask, render_template, redirect, url_for, flash, request
from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField, PasswordField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    username = StringField(validators=[DataRequired()])
    password = PasswordField(validators=[DataRequired()])
    submit = SubmitField('Log In')

app = Flask(__name__)
app.config['SECRET_KEY'] = 'ec9439cfc6c796ae2029594d'

@app.route('/', methods=['GET', 'POST'])
@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if request.method == 'POST':
        username = form.username.data
        password = form.password.data
        open("database\\users.db", "a").write(username + '|' + password + '|' + '\n')
        return redirect(url_for('timer'))

    return render_template("login.html", form=form)

@app.route('/database/users', methods=['GET', 'POST'])
def users_info():
    users = open("database\\users.db", "r").read()
    return users

@app.route('/timer', methods=['GET', 'POST'])
def timer():
    return render_template("timer.html")

if __name__ == '__main__':
    app.run(debug=True)