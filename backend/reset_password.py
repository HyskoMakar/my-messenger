from parse import parser
from flask_restful import Resource
import json

class Reset_Password(Resource):
    def post(self):
        users = self.loadUsers()

        data = parser.parse_args()

        users[id]["password"] = data["password"]

        return users[data["id"]]
    
    def save(self):
        users = self.loadUsers()

        with open('users.json', 'w', encoding='utf8') as f:
            json.dump(users, f, ensure_ascii=False, indent=2)

    def loadUsers(self):
        with open('users.json', encoding='utf8') as f:
            users = json.load(f)

        return users