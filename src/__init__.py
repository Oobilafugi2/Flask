from flask import Flask, jsonify
from flask_restx import Resource, Api

# set app instance
app = Flask(__name__)

# set api instance
api = Api(app)

# pull in development environment configs
app.config.from_object('src.config.DevelopmentConfig')


class Ping(Resource):
    def get(self):
        return {
            'status': 'success',
            'message': 'hello'
        }


api.add_resource(Ping, '/ping')

