from flask import Flask,  make_response
from parse import parser
from flask_restful import Resource
from dotenv import load_dotenv, dotenv_values 
import datetime
import json
import jwt
import re
import os

load_dotenv()

pat = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'

class Register(Resource):
    def post(self):
        users = self.loadUsers()

        data = parser.parse_args()

        lastKey = 0
        for key in users.keys():
            if users[key]["email"] == data["email"]:
                return "Bad request", 400
            
            key = int(key)
            if key > lastKey:
                lastKey = key

        newKey = str(lastKey + 1)

        eMail = data["email"]

        if not(re.match(pat, eMail)):
            return "Invalid Email", 400
        secret = os.getenv('secret')
        
        returnData = {
            "name": data["name"],
            "password": data["password"],
            "dateOfBirth": data["dateOfBirth"],
            "email": data["email"],
            "id": newKey
        }

        users[newKey] = returnData

        payload = {
            "exp": datetime.datetime.now(tz=datetime.timezone.utc) + datetime.timedelta(minutes=10),
            "sub": newKey,
            "email": data['email'],
            "password": data['password']
        }
                    
        atoken = jwt.encode(
            payload=payload,
            key=secret,
            algorithm='HS256')
                    
        rpayload = {
            "exp": datetime.datetime.now(tz=datetime.timezone.utc) + datetime.timedelta(days=14),
            "sub": newKey,
            "email": data['email'],
            "password": data['password']
        }
                    
        rtoken = jwt.encode(
            payload=rpayload,
            key=secret,
            algorithm='HS256')

        self.save(users)

        returnData['atoken'] = atoken


        resp = make_response(returnData)
        resp.set_cookie("rtoken", rtoken)

        return resp
    
    def save(self, users=dict):
        with open('users.json', 'w', encoding='utf8') as f:
            json.dump(users, f, ensure_ascii=False, indent=2)

    def loadUsers(self):
        with open('users.json', encoding='utf8') as f:
            users = json.load(f)

        return users
