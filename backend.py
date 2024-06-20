from flask import Flask
from flask_restful import Api, Resource, reqparse
import json

app = Flask(__name__)
api = Api()

with open('users.json', encoding='utf8') as f:
    users = json.load(f)

parser = reqparse.RequestParser()
parser.add_argument('id', type=str)
parser.add_argument('name', type=str)
parser.add_argument('password', type=str)
parser.add_argument('date-birth', type=str)

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

api.add_resource(Users, '/users/<string:id>')
api.add_resource(Register, '/register')
api.add_resource(Login, '/login')
api.init_app(app)

if __name__ == '__main__':
    app.run(debug=True, port=4000, host='127.0.0.1')