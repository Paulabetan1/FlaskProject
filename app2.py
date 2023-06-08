from flask_restful import Api, Resource
from flask import Flask
from flask_swagger import swagger
from flask_swagger_ui import get_swaggerui_blueprint

app = Flask(__name__)
api = Api(app)
wagger = swagger(app)

class HelloWorld(Resource):
    def get(self):
        """Return a hello world message"""
        return {'message': 'Hello World!'}

api.add_resource(HelloWorld, '/hello')

# Swagger documentation route
@app.route('/swagger')
def get_swagger():
    swag = swagger(app)
    swag['info']['version'] = "1.0"
    swag['info']['title'] = "My API"
    return jsonify(swag)

# Swagger UI route
SWAGGER_URL = '/swagger-ui'
API_URL = '/swagger'
swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': "My API"
    }
)
app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)