# bg_club
Application for Boys and Girls Club of America

Users will login to the application from the home page.

If a user is not registered they will click the register button from the home page where they will be redirected to the register page.
Once registered, they will be redirected back to the login page.

Only logged in users will have access to pages other than login/register.

New users will be set to Admin = False by default.  Admins can make other users admins or they can take away admin status.

There will be a '/admin' section that will contain forms for CRUD operations on various database models.  Records belonging to these models
will be able to be deleted, edited, created and viewed.

Only admin users will have access to the '/admin' section.  There will be an Admin link that displays in the navigation if the user is an 
admin.
