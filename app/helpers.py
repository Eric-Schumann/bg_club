from flask_admin import AdminIndexView, expose
from flask_login import login_required

#Helper file that includes needed class definitions for other extensions.

#Expose the '/' route from admin interface to override the index page.
class MyHomeView(AdminIndexView):
    @expose('/')
    @login_required
    def index(self):
        return self.render('_admin_index.html')