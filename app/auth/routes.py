from flask import render_template
from app.auth import authentication as at
from app.auth.models import User

@at.route('/')
def login_user():
    return render_template('auth/login.html')