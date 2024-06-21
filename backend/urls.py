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

        return users[newKey]
    
    def save(self):
        with open('users.json', 'w', encoding='utf8') as f:
            json.dump(users, f, ensure_ascii=False, indent=2)

class Login(Resource):
    def post(self, id:str):
        data = parser.parse_args()

        lastKey = 0
        for key in users.keys():
            if users[key]['name'] == data['name']:
                if users[key]['password'] == data['password']:
                    return users[id]
                else:
                    return "Wrong password", 403
            
            key = int(key)
            if key > lastKey:
                lastKey = key

        return "Not registered", 401
    
class Reset_Password(Resource):
    def post(self, id:str):
        data = parser.parse_args()["password"]

        users[id]["password"] = data

        return users[id]
    
    def save(self):
        with open('users.json', 'w', encoding='utf8') as f:
            json.dump(users, f, ensure_ascii=False, indent=2)