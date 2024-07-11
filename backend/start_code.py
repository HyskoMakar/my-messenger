from flask import Flask, make_response, render_template
from flask_restful import Api, reqparse, request

from pymongo import MongoClient
import pprint

import subprocess

from dotenv import load_dotenv
import datetime

import json
import os
import re

import jwt
from jwt.exceptions import InvalidSignatureError, ExpiredSignatureError

load_dotenv()

app = Flask('main')
app.config['secret_key'] = os.getenv('secret')

client = MongoClient('localhost', 27017)

db = client['messenger']
collection = db['users']

parser = reqparse.RequestParser()
parser.add_argument('name', type=str)
parser.add_argument('password', type=str)
parser.add_argument('dateOfBirth', type=str)
parser.add_argument('email', type=str)
parser.add_argument('id', type=str)
parser.add_argument('rtoken', type=str)

def loadUsers():
    collection = db['users']

    users = {}

    count = 1
    for user in collection.find():
        users[str(count)] = user

        count +=1

    return users