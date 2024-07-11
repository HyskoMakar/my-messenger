from start_code import *


@app.route('/reset-password', methods=['POST'])
def reset_password():
    if request.method == 'POST':
        users = loadUsers()

        data = parser.parse_args()

        users[id]["password"] = data["password"]

        return users[data["id"]]