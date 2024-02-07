from flask import request, abort
from resources.utils import template
from models.JokeModel import Joke
from flask_smorest import Blueprint
from db import db

blp = Blueprint('joke', __name__)

@blp.route('/jokes', methods=['POST', 'GET'])
def handle_jokes():
    if request.method == 'POST':
        joke_name = request.args.get("jokeName")
        joke_text = request.args.get("textJoke")
        data = {}
        if joke_name is not None and joke_text is not None :
            data['jokeName'] = joke_name
            data['textJoke'] = joke_text          
        if request.is_json:
            data = request.get_json()  
        if data == {} :
            abort(502)
        new_joke = Joke(jokeName=data['jokeName'], textJoke=data['textJoke'] )  
       
        db.session.add(new_joke)
        db.session.commit()
        data = {
            'jokeName': new_joke.jokeName,
            'textJoke': new_joke.textJoke
        }
        response = template('success', data, 'The joke was added correctly')
       
        return response

    if request.method == 'GET':
        jokes = Joke.query.all()
        data = [
            {
                "joke_id": joke.joke_id,
                "jokeName": joke.jokeName,
                "textJoke": joke.textJoke
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
            "jokeName": joke.jokeName,
            "textJoke": joke.textJoke}
        case 'PUT':
            data = request.get_json()
            joke.jokeName = data['jokeName']
            joke.textJoke = data['textJoke']
            db.session.add(joke)
            db.session.commit()
            response_data = {
            "jokeName": joke.jokeName,
            "textJoke": joke.textJoke}
            message = 'successfully updated.'
            return {"message": f"car {joke.jokeName} successfully updated"}
        case 'DELETE':
            db.session.delete(joke)
            db.session.commit()
            response_data = {
            "jokeName": joke.jokeName}
            message = 'successfully deleted.'
    
    response = template('success', response_data, message)
    return response