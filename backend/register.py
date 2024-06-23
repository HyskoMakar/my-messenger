from parser import parser
from users_file import users
from flask_restful import Resource
import json

class Register(Resource):
    def post(self):
        data = parser.parse_args()

        lastKey = 0
        for key in users.keys():
            if users[key]['name'] == data['name']:
                return "Bad request", 400
            
            key = int(key)
            if key > lastKey:
                lastKey = key

        newKey = str(lastKey + 1)

        users[newKey] = {
            "name": data["name"],
            "password": data["password"],
            "dateOfBirth": data["dateOfBirth"],
            "id": newKey
        }

        self.save()

        return users[newKey]
    
    def save(self):
        with open('users.json', 'w', encoding='utf8') as f:
            json.dump(users, f, ensure_ascii=False, indent=2)
