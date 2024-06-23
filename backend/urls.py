from parser import parser
from users_file import users
from flask_restful import Resource
from random import randint
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

class Login(Resource):
    def post(self):
        data = parser.parse_args()

        for key in users.keys():
            if users[key]['name'] == data['name']:
                if users[key]['password'] == data['password']:
                    return users[data["id"]], 200
                else:
                    return "Wrong password", 403
        return "Not registered", 401
    
class Reset_Password(Resource):
    def post(self):
        data = parser.parse_args()

        users[id]["password"] = data["password"]

        return users[data["id"]]
    
    def save(self):
        with open('users.json', 'w', encoding='utf8') as f:
            json.dump(users, f, ensure_ascii=False, indent=2)