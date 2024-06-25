from parser import parser
from users_file import users
from flask_restful import Resource
import base64
import json

class Login(Resource):
    def post(self):
        data = parser.parse_args()

        for key in users.keys():
            if users[key]["e-mail"] == data["e-mail"]:
                if users[key]["e-mail"] == data["e-mail"]:
                    secret_key = str(base64.b64encode(b'{str(data[realTime])}'))

                    users[key]["secret_key"] = secret_key

                    self.save()

                    return users[key], 200
                else:
                    return "Wrong password", 403
        return "Not registered", 401
    
    def save(self):
        with open('users.json', 'w', encoding='utf8') as f:
            json.dump(users, f, ensure_ascii=False, indent=2)