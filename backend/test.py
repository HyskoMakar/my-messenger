import base64
from time import time

print(base64.b64encode(b'{str(time())}'))