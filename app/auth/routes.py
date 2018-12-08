from flask import render_template, redirect, flash, url_for
from app.auth import authentication as at
from app.auth.models import User
from app.auth.forms import RegistrationForm, LoginForm
from app import bcrypt

#Root URL for application
@at.route('/', methods=["GET", "POST"])
def login_user():
    form = LoginForm()

    if form.validate_on_submit():
        user = User.query.filter_by(user_email=form.email.data).first()

        if user.user_password == bcrypt.generate_password_hash(form.password.data).decode('utf-8'):
            return redirect(url_for('authentication.login_success'))
        else:
            flash('Login failed.', category='error')

    return render_template('auth/login.html', form=form)

@at.route('/registration', methods=["GET", "POST"])
def register_user():
    form = RegistrationForm()

    if form.validate_on_submit():
        if User.query.filter_by(user_email=form.email.data).first():
            flash('Email already exists.')
        else:
            User.create_user(form.first_name.data, form.last_name.data, form.email.data, 
                bcrypt.generate_password_hash(form.password.data).decode('utf-8'))
            flash('User successfully created.  Please log in.', category='success')
            return redirect(url_for('authentication.login_user'))

    return render_template('auth/registration.html', form=form)

@at.route('/success')
def login_success():
    return render_template('auth/success.html')