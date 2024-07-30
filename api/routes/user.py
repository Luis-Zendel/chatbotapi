from flask import Blueprint
from flask import Flask, render_template, request, redirect
from flask_pymongo import pymongo
from flask import jsonify
import db
import os
from config import config
from datetime import datetime
import jsonfun
import jwt
from functools import wraps
from datetime import date
from datetime import datetime
from decode import token_required

user_bp = Blueprint('users',__name__ )

@user_bp.route('/get', methods = ['GET'])
@token_required
def obtenerComentarios():
    return "Hello to user"

## Estrctura esperada 
@user_bp.route('/save', methods = ['POST'])
def saveUser():
    print("Save User => /users/save")
    if(request.method == 'POST'):
        data = request.json
        email = data.get('email') 
        account = data.get('account')
        user = data.get('user')
        print(email , "_-+++++++____")
        exist_email = db.user_collection.find({"email": email})
        get_email_list = list(exist_email)
        num = len(get_email_list)
        print(num)
        if num == 0:
            data = request.json
            print(data)
            email= data.get('email')
            now_date = datetime.now()
            user_to_save = {
                "email": email,
                "user": user,
                "account": account,
                "date": now_date
            }
            userDB = db.user_collection.insert_one(user_to_save)
            print(userDB)
            response_message = {"message": "The user was creat"}
            return jsonify(response_message), 201
        else:
            response_message = {"message": "The user exist"}
            return jsonify(response_message), 200
