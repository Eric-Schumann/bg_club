from flask import render_template, session
from app.bins import bins   

@bins.route('/success')
def success():
    return render_template('bins/success.html')