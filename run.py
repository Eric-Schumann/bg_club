from app import create_app
from app import db
from app.auth.models import User

if __name__ == '__main__':
    app = create_app('dev')
    app.run()
    with app.app_context():
        db.create_all()