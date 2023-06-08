from db import db
from config_database import FULL_URL_DB
from flask import Flask
from flask_migrate import Migrate
from resources.joke import blp as joke
from resources.math import blp as math 
from resources.errors import blp as errors
from flask import request, render_template, url_for
from werkzeug.utils import redirect
from resources.utils import GetJokes


def create_app():

    app = Flask(__name__)
    # app.config["API_TITLE"] = "Reto"
    # app.config["API_VERSION"] = "v1"
    # app.config["OPENAPI_VERSION"] = "4.18.3"
    # app.config["OPENAPI_URL_PREFIX"] = "/1"
    # app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"
    # app.config[
    #     "OPENAPI_SWAGGER_UI_URL"
    # ] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"
    print(FULL_URL_DB)
    app.config['SQLALCHEMY_DATABASE_URI'] = FULL_URL_DB
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)
    migrate = Migrate()
    migrate.init_app(app, db)
    app.register_blueprint(joke)
    app.register_blueprint(math)
    app.register_blueprint(errors)
    return app

app = create_app()

@app.route('/')
@app.route('/index')
@app.route('/index.html',  methods = ['GET','POST'])
def start():
    return render_template('index.html') 

@app.route('/option',methods = ['GET','POST'])
def option():
     if request.method == 'POST':
        option = str(request.form['option']).lower()
        return redirect(url_for('show_joke', option=option))

@app.route('/<option>')
def show_joke(option):
    joke = GetJokes(option)
    result = joke.all_jokes()        
    return render_template('show_joke.html', option = option, joke = result ) 

@app.errorhandler(400)
def bad_request(error):
    return render_template('error400.html', error = error),400

@app.errorhandler(502)
def bad_request(error):
    return render_template('error400.html', error = error),502