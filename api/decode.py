import jwt
from flask import jsonify
from functools import wraps 

# Decodificación del JWT

def tokenRequired(f):
    @wraps(f)
    def verifyToken(*args, **kwargs):
        token = ""
        if 'Authorization' in request.headers:
            token = request.headers['Authorization'].split()[1]
        if not token:
            return jsonify({'message':"Token is missing"}), 403

        try:
            decoded_token = jwt.decode(token,secret, algorithms=["HS256"])
        except jwt.ExpiredSignatureError:
            return jsonify({'message':"Token has expired"}), 403
        except jwt.InvalidTokenError as e:
            print(f"Token is invalid: {e}")
            return jsonify({'message':"Token is invalid"}), 403
        return decoded_token

