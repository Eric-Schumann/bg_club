from flask import Blueprint

bins = Blueprint('bins', __name__, template_folder='templates')

from app.bins import routes