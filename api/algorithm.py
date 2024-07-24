import jwt
from flask import jsonify
from functools import wraps 

print("Iniciando decodificacion")

token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VySWQiOiIxMDk5MjA2MTQzMjIxOTUzMzEyODUiLCJlbWFpbCI6InNhMzM3MzUyQHVhZWguZWR1Lm14IiwiaWF0IjoxNzIxNzc5MTgzLCJleHAiOjE3MjQzNzExODN9.o8GgaxDskhcFWC4Xjh_har9Nzk8zGmomlm1d-dBZIkM"
secret = "OQaNHui9urkgzSD6TXgi+3MPuhMBpMn3rbt0GPf1whg="
decoded_token = jwt.decode(token,secret, algorithms=["HS256"])
print("TOKEN ")
print(decoded_token)
