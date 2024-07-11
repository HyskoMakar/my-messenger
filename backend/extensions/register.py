from start_code import *

load_dotenv()

pat = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'

@app.route('/register', methods=['POST'])
def register():
    if request.method == 'POST':
        users = loadUsers()

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
            "email": data["email"]
        }

        insertData = returnData

        collection.insert_one(insertData)

        returnData['_id'] = ''

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

        returnData['atoken'] = atoken

        resp = make_response(returnData)
        resp.set_cookie("rtoken", rtoken)

        return resp