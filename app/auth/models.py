from app import db
from datetime import datetime
from app import bcrypt

class User(db.Model):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(100))
    user_email = db.Column(db.String(50), unique=True, index=True)
    user_password = db.Column(db.String(100))
    user_registration_date = db.Column(db.DateTime, default=datetime.now)
    user_is_admin = db.Column(db.Boolean, default=False)

    @classmethod
    def create_user(cls, name, email, password, is_admin):
        user = cls(
            user_name = name,
            user_email = email,
            user_password = bcrypt.generate_password_hash(password).decode('utf-8'),
            user_is_admin = is_admin
        )

        db.session.add(user)
        db.session.commit()
        return user