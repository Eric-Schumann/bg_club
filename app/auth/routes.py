from flask import render_template, redirect, flash, url_for, session
from app.auth import authentication as at
from app.auth.models import User
from app.auth.forms import RegistrationForm, LoginForm
from flask_bcrypt import check_password_hash
from app import login_manager
from flask_login import login_user, login_required, logout_user

@login_manager.user_loader
def load_user(id):
    return User.query.get(int(id))

#Root URL for application
@at.route('/', methods=["GET", "POST"])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        user = User.query.filter_by(user_email=form.email.data).first()
        if check_password_hash(user.user_password, form.password.data):
            login_user(user)
            session['user_first_name'] = user.user_first_name
            return redirect(url_for('authentication.login_success'))
        else:
            flash('Invalid email or password.', category='error')

    return render_template('auth/login.html', form=form)

@at.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out.', category='success')
    return redirect(url_for('authentication.login'))

@at.route('/registration', methods=["GET", "POST"])
def register_user():
    form = RegistrationForm()

    if form.validate_on_submit():
        if User.query.filter_by(user_email=form.email.data).first():
            flash('Email already exists.')
        else:
            User.create_user(form.first_name.data, form.last_name.data, form.email.data, form.password.data)
            flash('User successfully created.  Please log in.', category='success')
            return redirect(url_for('authentication.login'))

    return render_template('auth/registration.html', form=form)

@at.route('/success')
@login_required
def login_success():
    return render_template('auth/success.html', user=session['user_first_name'])

@at.route('/unauthorized')
def unauthorized():
    return render_template('auth/unauthorized.html')