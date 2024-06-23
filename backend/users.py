from parser import parser
from users_file import users
from flask_restful import Resource
import json

class Users(Resource):
    def get(self, id:str):
        if id == '':
            return users
        else:
            return users[id]
    
    def put(self, id:str):
        users[id] = parser.parse_args()
        
        self.save()
        
        return users[id]
    
    def save(self):
        with open('users.json', 'w', encoding='utf8') as f:
            json.dump(users, f, ensure_ascii=False, indent=2)