from flask import Flask,  make_response
from parser import parser
from flask_restful import Resource
from dotenv import load_dotenv, dotenv_values 
import json
import jwt
import re
import os

with open('users.json', encoding='utf8') as f:
    users = json.load(f)

load_dotenv()

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

        eMail = data["e-mail"]

        if not(re.match(pat, eMail)):
            return "Invalid Email", 400

        payloadData = {
            "name": data["name"],
            "password": data["password"],
            "dateOfBirth": data["dateOfBirth"],
            "e-mail": data["e-mail"],
            "id": newKey
        }

        secret = os.getenv('secret')

        token = jwt.encode(
            payload=payloadData,
            key=secret,
            algorithm='HS256'
        )

        users[newKey] = payloadData

        self.save()

        resp = make_response(users[newKey])
        resp.headers['token'] = token

        return resp
    
    def save(self):
        with open('users.json', 'w', encoding='utf8') as f:
            json.dump(users, f, ensure_ascii=False, indent=2)
