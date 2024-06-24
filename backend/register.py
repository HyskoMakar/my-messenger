from parser import parser
from users_file import users
from flask_restful import Resource
from time import time
import base64
import json
import re

import real_time

pat = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'

class Register(Resource):
    def post(self):
        data = parser.parse_args()

        lastKey = 0
        for key in users.keys():
            if users[key]["e-mail"] == data["e-mail"]:
                return "Bad request", 400
            
            key = int(key)
            if key > lastKey:
                lastKey = key

        newKey = str(lastKey + 1)

        if not(re.match(pat, str(data["e-mail"]))):
            return "Invalid Email", 400
        
        secret_key = str(base64.b64encode(b'{str(real_time.realTime)}'))

        users[newKey] = {
            "name": data["name"],
            "password": data["password"],
            "dateOfBirth": data["dateOfBirth"],
            "e-mail": data["e-mail"],
            "secret_key": secret_key,
            "id": newKey
        }

        self.save()

        return users[newKey]
    
    def save(self):
        with open('users.json', 'w', encoding='utf8') as f:
            json.dump(users, f, ensure_ascii=False, indent=2)
