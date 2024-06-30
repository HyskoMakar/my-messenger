import datetime
from flask import make_response, request
from backend.parse import parser
from flask_restful import Resource

from dotenv import load_dotenv, dotenv_values 

import jwt
from jwt.exceptions import InvalidSignatureError, ExpiredSignatureError

import json

import os

load_dotenv()

class Refresh_token(Resource):
    def post(self):
        users = self.loadUsers()

        data = parser.parse_args()

        secret = os.getenv('secret')

        data = jwt.decode(
            data['rtoken'],
            key=secret, 
            leeway=datetime.timedelta(days=14),
            algorithms=['HS256', ]
        )

        for key in users.keys():
            if users[key]["email"] == data["email"]:
                if users[key]["password"] == data["password"]:
                    payload = {
                        "exp": datetime.datetime.now(tz=datetime.timezone.utc) + datetime.timedelta(minutes=10),
                        "sub": users[key]['id'],
                        "email": data['email'],
                        "password": data['password']
                    }
                    
                    token = jwt.encode(
                        payload=payload,
                        key=secret,
                        algorithm='HS256')
                    
                    payload = {
                        "exp": datetime.datetime.now(tz=datetime.timezone.utc) + datetime.timedelta(days=14),
                        "sub": users[key]['id'],
                        "email": data['email'],
                        "password": data['password']
                    }
                    
                    rtoken = jwt.encode(
                        payload=payload,
                        key=secret,
                        algorithm='HS256')
                    
                    returnData = {}

                    returnData['token'] = token
                    returnData['rtoken'] = rtoken

                    resp = make_response(returnData)

                    return resp
                else:
                    return "Wrong password", 403
        return "Not registered", 401
    
    def loadUsers(self):
        with open('users.json', encoding='utf8') as f:
            users = json.load(f)

        return users