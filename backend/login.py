import datetime
from flask import make_response
from parse import parser
from flask_restful import Resource
from dotenv import load_dotenv
import jwt
import json
import os

load_dotenv()

class Login(Resource):
    def post(self):
        users = self.loadUsers()

        data = parser.parse_args()

        for key in users.keys():
            if users[key]["email"] == data["email"]:
                if users[key]["password"] == data["password"]:
                    secret = os.getenv('secret')

                    payload = {
                        "exp": datetime.datetime.now(tz=datetime.timezone.utc) + datetime.timedelta(minutes=10),
                        "sub": users[key]['id'],
                        "email": data['email'],
                        "password": data['password']
                    }
                    
                    atoken = jwt.encode(
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
                    
                    returnData = users[key]

                    returnData['atoken'] = atoken

                    resp = make_response(returnData)
                    resp.set_cookie("rtoken", rtoken)

                    return resp
                else:
                    return "Wrong password", 403
        return "Not registered", 401
    
    def loadUsers(self):
        with open('users.json', encoding='utf8') as f:
            users = json.load(f)

        return users