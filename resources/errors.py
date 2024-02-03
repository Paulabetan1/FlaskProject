
from flask import render_template
from flask_smorest import Blueprint

blp = Blueprint('errors', __name__)

@blp.errorhandler(400)
def bad_request(error):
    return render_template('error400.html', error = error),400

@blp.errorhandler(502)
def bad_request(error):
    return render_template('error400.html', error = error),502