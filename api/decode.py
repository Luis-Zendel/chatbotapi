from dotenv import load_dotenv
import jwt
import os
from flask import request, jsonify
from functools import wraps

load_dotenv()
variable  = os.environ.get('SECRET_KEY')

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        auth = request.headers.get('Authorization')
        if not auth:
            return jsonify({'message': 'Token is missing!'}), 403
        
        try:
            token_value = request.headers["Authorization"].split(" ")[1]
            data = jwt.decode(token_value, variable, algorithms=["HS256"])
        except jwt.ExpiredSignatureError:
            return jsonify({'message': 'Token has expired!'}), 403
        except jwt.InvalidTokenError:
            return jsonify({'message': 'Invalid token!'}), 403
        
        return f(*args, **kwargs)
    
    return decorated
