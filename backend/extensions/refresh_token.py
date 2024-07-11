from start_code import *

load_dotenv()

@app.route('/refresh-token', methods=['POST'])
def refresh_token():
    if request.method == 'POST':
        users = loadUsers()

        data = request.cookies.get('rtoken')

        secret = os.getenv('secret')

        data = jwt.decode(
            data,
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
                    returnData['_id'] = ''

                    resp = make_response(returnData)
                    resp.set_cookie('rtoken', rtoken)

                    return resp
                else:
                    return "Wrong password", 403
        return "Not registered", 401