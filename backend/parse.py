from flask_restful import reqparse

parser = reqparse.RequestParser()
parser.add_argument('name', type=str)
parser.add_argument('password', type=str)
parser.add_argument('dateOfBirth', type=str)
parser.add_argument('email', type=str)
parser.add_argument('id', type=str)
parser.add_argument('rtoken', type=str)