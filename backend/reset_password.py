from parser import parser
from flask_restful import Resource
import json

class Reset_Password(Resource):
    def post(self):
        data = parser.parse_args()

        users[id]["password"] = data["password"]

        return users[data["id"]]
    
    def save(self):
        with open('users.json', 'w', encoding='utf8') as f:
            json.dump(users, f, ensure_ascii=False, indent=2)