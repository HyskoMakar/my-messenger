from parse import parser
from flask_restful import Resource
from flask import request
from dotenv import load_dotenv, dotenv_values 
import datetime
import json
import jwt
import os

load_dotenv()
class Users(Resource):
    def get(self):
        users = self.loadUsers()

        secret = os.getenv('secret')

        atoken = request.headers.get('atoken')

        try:
            _data = jwt.decode(
                atoken,
                key=secret, 
                leeway=datetime.timedelta(minutes=10),
                algorithms=['HS256', ]
            )
        except:
            return 'Invalid signature', 401

        data = users[_data['sub']]

        if _data['email'] == data['email'] and _data['password'] == data['password']:
            return users[_data['sub']]
        return '''It isn't your acccount!''', 401
    
    def put(self):
        users = self.loadUsers()

        users[id] = parser.parse_args()
        
        self.save(users)
        
        return users[id]
    
    def save(self, users):
        with open('users.json', 'w', encoding='utf8') as f:
            json.dump(users, f, ensure_ascii=False, indent=2)

    def loadUsers(self):
        with open('users.json', encoding='utf8') as f:
            users = json.load(f)

        return users
