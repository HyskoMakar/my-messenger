from flask import make_response, request
from parser import parser
from flask_restful import Resource

from dotenv import load_dotenv, dotenv_values 

import jwt
from jwt.exceptions import InvalidSignatureError, ExpiredSignatureError

import json

import os

with open('users.json', encoding='utf8') as f:
    users = json.load(f)

load_dotenv()

class Login(Resource):
    def post(self):
        data = parser.parse_args()

        for key in users.keys():
            if users[key]["e-mail"] == data["e-mail"]:
                if users[key]["password"] == data["password"]:
                    token = request.headers.get('token')

                    secret = os.getenv('secret')

                    if token != '':
                        try:
                            jwt.decode(
                                token,
                                key=secret, 
                                algorithms=['HS256', ])
                        except InvalidSignatureError:
                            return 'Signature verification failed', 401
                        
                        header_data = jwt.get_unverified_header(token)
                        jwt.decode(
                            token, 
                            key=secret, 
                            algorithms=[header_data['alg'], ])
                        try:
                            pass
                        except ExpiredSignatureError:
                            return 'Signature was expired', 401
                    else:
                        token = jwt.encode(
                            payload=payloadData,
                            key=secret,
                            algorithm='HS256'
                        )

                    resp = make_response(users[key])
                    resp.headers['token'] = token

                    return resp
                else:
                    return "Wrong password", 403
        return "Not registered", 401