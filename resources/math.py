from flask import request, abort
from resources.utils import template, Mathmcm
from flask_smorest import Blueprint

blp = Blueprint('math', __name__)

@blp.route('/math')
def show_numbers():
    numbers = request.args.get("numbers")
    number = request.args.get("number")
    if numbers is None and number is None:
        abort(404)
    if numbers:
        mcm = Mathmcm(numbers)
        result= mcm.get()
        data = {"MCM is:":result}
    if number:
        data = {"Number +1:":int(number)+1}
    
    response = template('success', data, "")
    return response
 
    