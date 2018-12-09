from flask import render_template, redirect, flash, url_for, session
from app.auth import authentication as at
from app.auth.models import User
from app.auth.forms import RegistrationForm, LoginForm, ResetPasswordForm
from flask_bcrypt import check_password_hash, generate_password_hash
from app import login_manager, db
from flask_login import login_user, login_required, logout_user
from app.helpers import populate_session

@login_manager.user_loader
def load_user(id):
    return User.query.get(int(id))

#Root URL for application
@at.route('/', methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(user_email=form.email.data).first()
        if user:
            if check_password_hash(user.user_password, 'password01'):
                populate_session(user)
                return redirect(url_for('authentication.reset_password'))
            if check_password_hash(user.user_password, form.password.data):
                login_user(user)
                populate_session(user)
                return redirect(url_for('bins.success'))
            else:
                flash('Invalid email or password.', category='error')
        else:
            flash('Invalid user.  Contact administrator or try again.', category='error')
    return render_template('auth/login.html', form=form)

@at.route('/logout')
@login_required
def logout():
    logout_user()
    session.clear()
    flash('You have been logged out.', category='success')
    return redirect(url_for('authentication.login'))

@at.route('/registration', methods=["GET", "POST"])
@login_required
def register_user():
    if not session['user_is_admin']:
        return redirect(url_for('authentication.unauthorized'))

    form = RegistrationForm()

    if form.validate_on_submit():
        if User.query.filter_by(user_email=form.email.data).first():
            flash('Email already exists.')
        else:
            user = User.create_user(form.first_name.data, form.last_name.data, form.email.data)
            flash(f'{user.user_email} successfully created.', category='success')

    return render_template('auth/registration.html', form=form)

@at.route('/unauthorized')
def unauthorized():
    return render_template('auth/unauthorized.html')

@at.route('/reset', methods=["GET", "POST"])
def reset_password():
    form = ResetPasswordForm()

    if form.validate_on_submit():
        user = User.query.filter_by(user_email=session['user_email']).first()
        user.user_password = generate_password_hash(form.password.data).decode('utf-8')
        db.session.add(user)
        db.session.commit()
        login_user(user)
        return redirect(url_for('bins.success'))
    return render_template('auth/reset_password.html', form=form)