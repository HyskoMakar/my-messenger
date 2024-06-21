from flask import Flask
from flask_restful import Api, Resource
from urls import *

app = Flask(__name__)
api = Api()

api.add_resource(Users, '/users/<string:id>')
api.add_resource(Register, '/register')
api.add_resource(Login, '/login')
api.add_resource(Reset_Password, '/reset-password')
api.init_app(app)

if __name__ == '__main__':
    app.run(debug=True, port=4000, host='127.0.0.1')