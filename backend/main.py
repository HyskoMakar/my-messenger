from flask import Flask
from flask_restful import Api
from users import *
from register import *
from login import *
from reset_password import *
from refresh_token import *

app = Flask(__name__)
api = Api()

api.add_resource(Users, '/me')
api.add_resource(Register, '/register')
api.add_resource(Login, '/login')
api.add_resource(Refresh_token, '/refresh-token')
api.add_resource(Reset_Password, '/reset-password')
api.init_app(app)

if __name__ == '__main__':
    app.run(debug=True, port=4000, host='127.0.0.1')