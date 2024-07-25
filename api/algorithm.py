import jwt
from dotenv import load_dotenv
import os

load_dotenv()
secret = os.environ.get('SECRET_KEY')
token =  os.environ.get('TOKEN_EXAMPLE')

decoded_token = jwt.decode(token,secret, algorithms=["HS256"])
print("TOKEN ")
print(decoded_token)
