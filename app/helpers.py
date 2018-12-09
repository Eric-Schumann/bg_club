from flask import session
from flask_admin import AdminIndexView, expose
from flask_login import login_required

#Helper file that includes needed class definitions for other extensions.

#Expose the '/' route from admin interface to override the index page.
class MyHomeView(AdminIndexView):
    @expose('/')
    @login_required
    def index(self):
        return self.render('_admin_index.html')

def populate_session(user):
    session['user_first_name'] = user.user_first_name
    session['user_email'] = user.user_email
    session['user_is_admin'] = user.user_is_admin