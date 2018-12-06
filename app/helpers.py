from flask_admin import AdminIndexView, expose

class MyHomeView(AdminIndexView):
    @expose('/')
    def index(self):
        return self.render('_admin_index.html')