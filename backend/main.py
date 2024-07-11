from extensions.users import *
from extensions.register import *
from extensions.login import *
from extensions.reset_password import *
from extensions.refresh_token import *
from websockets import *

if __name__ == '__main__':
    app.run(debug=True, port=2000)
    client.close()