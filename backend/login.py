from parser import parser
from users_file import users
from flask_restful import Resource
import json

class Login(Resource):
    def post(self):
        data = parser.parse_args()

        for key in users.keys():
            if users[key]["e-mail"] == data["e-mail"]:
                if users[key]["e-mail"] == data["e-mail"]:
                    return users[data["id"]], 200
                else:
                    return "Wrong password", 403
        return "Not registered", 401