from flask import Blueprint
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
import jwt
from functools import wraps
from decode import tokenRequired
from datetime import date
from datetime import datetime

user_bp = Blueprint('users',__name__ )

@user_bp.route('/get', methods = ['GET'])
def obtenerComentarios():
    return "Hello to user"

## Estrctura esperada 
@user_bp.route('/save', methods = ['POST'])
def saveUser():
    print("Save User => /users/save")
    if(request.method == 'POST'):
        exist_email = db.user_collection({"email": email})
        get_email_list = list(exist_email)
        num = len(get_email_list)
        if num == 0:
            data = request.json
            print(data)
            email= data.get('email')
            name = data.get('name')
            now_date = datetime.now()
            user_to_save = {
                "email": email,
                "name": name,
                "date": now_date
            }
            userDB = db.user_collection.insert_one(user_to_save)
            print(userDB)
            response_message = {"message": "The user was creat"}
            return jsonify(response_message), 201
        else:
            response_message = {"message": "The user exist"}
            return jsonify(response_message), 200
