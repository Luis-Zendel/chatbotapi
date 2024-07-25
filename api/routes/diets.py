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
from decode import token_required

diet_bp = Blueprint('diets',__name__ )
## Open AI configuration 
load_dotenv()
variable = os.environ.get('OPENAI_KEY')
context = {"role": "system","content": "Eres un asistente muy utíl especialista en nutrición y alimentación que tienes como cobjetivo en base a tu experiencia proporcionar al usuairo un plan alimenticio personalizado"}
messages = [context]
clientOpenAI = OpenAI(api_key= variable) 
openAIModel = "gpt-3.5-turbo"

@diet_bp.route('/get', methods = ['GET'])
@token_required
def obtenerComentarios():
    return "Hello to comment"

## Estrctura esperada 
@diet_bp.route('/save', methods = ['POST'])
@token_required
def saveDiet():
    print("Save Comment => /diets/save")
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

@diet_bp.route('/generate', methods=['POST'])
@token_required
def generateDiet():
    print("Generate Diet => /diets/generate")
    if request.method == 'POST':
        data = request.json
        email = data.get('email') 
        existDiet = db.diet_collection.find({"email": email})
        getDietList = list(existDiet)
        getDietNumber = len(getDietList)
        if(email == "sa337352@uaeh.edu.mx"):
            getDietNumber = 0
        print(getDietNumber)
        if getDietNumber > 2:
            print("No es posible generar una dieta " + email)
            response_message = {"message": "No fue posible generar una dieta, ya a utilizado esta función anteriormente", "response" : ""}
            return jsonify(response_message), 200
            ## Generar dieta, hacer petición
        else:
            print("Se va generar una dieta")
            prompt = data.get('prompt')
            name = data.get("name")
            print("Prompt")
            print(prompt)
            messages.append({"role": "user", "content": prompt})
            response = clientOpenAI.chat.completions.create(model=openAIModel, messages=messages)
            response_content = response.choices[0].message.content
            messages.append({"role": "assistant", "content": response_content})
            print(f"Respuesta: {response_content} | Fin ")
            response_diet = json.loads(response_content)
            print(f"DietJSON: {response_diet} | FIN")
            now_date = datetime.now()
            diet_name = str(getDietNumber+1)+ name
            diet_to_save = {
                "email": email,
                "name": diet_name,
                "prompt": prompt,
                "diet": response_diet,
                "date": now_date,
            }
            dietDB = db.diet_collection.insert_one(diet_to_save)
            print(dietDB)
            response_message = {"message": "Su dieta fue generada correctamente ", "data" : response_diet, "code": 201}
            print(response_message)
            return jsonify(response_message), 201