from flask import request, abort
from resources.utils import template
from models.JokeModel import Joke
from flask_smorest import Blueprint
from db import db

blp = Blueprint('joke', __name__)

@blp.route('/jokes', methods=['POST', 'GET'])
def handle_jokes():
    if request.method == 'POST':
        joke_name = request.args.get("joke_name")
        text_joke = request.args.get("text_joke")
        data = {}
        if joke_name is not None and text_joke is not None :
            data['joke_name'] = joke_name
            data['text_joke'] = text_joke          
        if request.is_json:
            data = request.get_json()  
        if data == {} :
            abort(502)
        new_joke = Joke(joke_name=data['joke_name'], text_joke=data['text_joke'] )  
       
        db.session.add(new_joke)
        db.session.commit()
        data = {
            'joke_name': new_joke.joke_name,
            'text_joke': new_joke.text_joke
        }
        response = template('success', data, 'The joke was added correctly')
       
        return response

    if request.method == 'GET':
        jokes = Joke.query.all()
        data = [
            {   "joke_id": joke.joke_id,
                "joke_name": joke.joke_name,
                "text_joke": joke.text_joke
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
            "joke_name": joke.joke_name,
            "text_joke": joke.text_joke}
        case 'PUT':
            data = request.get_json()
            joke.joke_name = data['joke_name']
            joke.text_joke = data['text_joke']
            db.session.add(joke)
            db.session.commit()
            response_data = {
            "joke_name": joke.joke_name,
            "text_joke": joke.text_joke}
            message = 'successfully updated.'
            return {"message": f"{joke.joke_name} successfully updated"}
        case 'DELETE':
            db.session.delete(joke)
            db.session.commit()
            response_data = {
            "joke_name": joke.joke_name}
            message = 'successfully deleted.'
    
    response = template('success', response_data, message)
    return response