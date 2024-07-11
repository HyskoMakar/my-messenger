from start_code import *

load_dotenv()

@app.route('/me', methods=['GET', 'PUT'])
def users():
    if request.method == 'GET':
        users = loadUsers()

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

        data['_id'] = ''

        if _data['email'] == data['email'] and _data['password'] == data['password']:
            return data
        return '''It isn't your acccount!''', 401
    
    elif request.method == 'PUT':
        users = loadUsers()

        users[id] = parser.parse_args()
        
        return users[id]



