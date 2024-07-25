from flask import Flask, render_template, request, redirect
from flask_pymongo import pymongo
from flask import jsonify
import json 
from flask_cors import CORS
from openai import OpenAI
from dotenv import load_dotenv
import db
import os
from config import config
from datetime import datetime
import jsonfun
from routes.comment import comment_bp
from routes.user import user_bp
from routes.diets import diet_bp
import jwt
from functools import wraps
"""

"""
load_dotenv()

def create_app(enviroment):
    app = Flask(__name__)
    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
    app.register_blueprint(user_bp, url_prefix='/users' )
    app.register_blueprint(diet_bp, url_prefix='/diets' )
    app.register_blueprint(comment_bp, url_prefix='/comments' )
    CORS(app)
    app.config.from_object(enviroment)
    return app


enviroment = config['development']
app = create_app(enviroment)

"""
1)CREAR USUARIO 
    Validar que el usuario no existe 
    Crear usuario y contraseña 
"""



        
            


if __name__ == '__main__':
    app.run(port=8000)