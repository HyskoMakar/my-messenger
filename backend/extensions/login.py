from start_code import *

load_dotenv()

@app.route('/login', methods=['POST'])
def login():
    if request.method == 'POST':
        users = loadUsers()

        data = parser.parse_args()

        for key in users.keys():
            if users[key]["email"] == data["email"]:
                if users[key]["password"] == data["password"]:
                    secret = os.getenv('secret')

                    payload = {
                        "exp": datetime.datetime.now(tz=datetime.timezone.utc) + datetime.timedelta(minutes=10),
                        "sub": key,
                        "email": data['email'],
                        "password": data['password']
                    }
                    
                    atoken = jwt.encode(
                        payload=payload,
                        key=secret,
                        algorithm='HS256')
                    
                    payload = {
                        "exp": datetime.datetime.now(tz=datetime.timezone.utc) + datetime.timedelta(days=14),
                        "sub": key,
                        "email": data['email'],
                        "password": data['password']
                    }
                    
                    rtoken = jwt.encode(
                        payload=payload,
                        key=secret,
                        algorithm='HS256')
                    
                    returnData = users[key]

                    returnData['atoken'] = atoken
                    returnData['_id'] = ''

                    resp = make_response(returnData)
                    resp.set_cookie("rtoken", rtoken)

                    return resp
                else:
                    return "Wrong password", 403
        return "Not registered", 401