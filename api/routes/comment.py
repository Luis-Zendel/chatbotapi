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
from datetime import date
from datetime import datetime

comment_bp = Blueprint('comments',__name__ )

@comment_bp.route('/get', methods = ['GET'])
def obtenerComentarios():
    return "Hello to comment"

## Estrctura esperada 
@comment_bp.route('/save', methods = ['POST'])
def saveComment():
    print("Save Comment => /comments/save")
    if(request.method == 'POST'):
        data = request.json
        print(data)
        email= data.get('email')
        ## Verificar si existe el email en la base de datos 
        comment = data.get('comment')
        title = data.get('title')
        now_date = datetime.now()
        comment_to_save = {
            "email": email,
            "title": title,
            "comment": comment,
            "date": now_date
        }
        commentCB = db.comment_collection.insert_one(comment_to_save)
        print(commentCB)
        response_message = {"message": "The comment was creat"}
        return jsonify(response_message), 201
