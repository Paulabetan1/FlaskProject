from flask import request, abort
from resources.utils import template
from models.JokeModel import Joke
from flask_smorest import Blueprint
from db import db

blp = Blueprint('joke', __name__)

@blp.route('/jokes', methods=['POST', 'GET'])
def handle_jokes():

    if request.method == 'POST':
        joke_name = request.args.get("nombreChiste")
        joke_text = request.args.get("textoChiste")
        data = {}
        if joke_name is not None and joke_text is not None :
            data['nombreChiste'] = joke_name
            data['textoChiste'] = joke_text          
        if request.is_json:
            data = request.get_json()  
        if data == {} :
            abort(502)
        new_joke = Joke(nombreChiste=data['nombreChiste'], textoChiste=data['textoChiste'] )  
        db.session.add(new_joke)
        db.session.commit()
        data = {
            'nombreChiste': new_joke.nombreChiste,
            'textoChiste': new_joke.textoChiste
        }
        response = template('success', data, 'El chiste se agrego correctamente')
       
        return response

    if request.method == 'GET':
        jokes = Joke.query.all()
        data = [
            {
                "id": joke.id,
                "nombreChiste": joke.nombreChiste,
                "textoChiste": joke.textoChiste
            } for joke in jokes]
        
        response = template('success', data, '')
        return response

@blp.route('/jokes/<joke_id>', methods=['GET', 'PUT', 'DELETE',])
def handle_joke(joke_id):
    joke = Joke.query.get_or_404(joke_id)
    message =''
    match request.method:
        case 'GET':
            response_data = {
            "nombreChiste": joke.nombreChiste,
            "textoChiste": joke.textoChiste}
        case 'PUT':
            data = request.get_json()
            joke.nombreChiste = data['nombreChiste']
            joke.textoChiste = data['textoChiste']
            db.session.add(joke)
            db.session.commit()
            response_data = {
            "nombreChiste": joke.nombreChiste,
            "textoChiste": joke.textoChiste}
            message = 'successfully updated.'
            return {"message": f"car {joke.nombreChiste} successfully updated"}
        case 'DELETE':
            db.session.delete(joke)
            db.session.commit()
            response_data = {
            "nombreChiste": joke.nombreChiste}
            message = 'successfully deleted.'
    
    response = template('success', response_data, message)
    return response