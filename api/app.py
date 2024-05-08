from flask import Flask, render_template, request, redirect
from flask_pymongo import pymongo
from flask import jsonify
import json 
from flask_cors import CORS
from openai import OpenAI
from dotenv import load_dotenv
import db
import algorithm
import os
from config import config
from datetime import datetime
import jsonfun
from routes.comment import comment_bp
import re
"""
-Definir rutas de usarios 
-Funcionalidad de crud 
-Crear un nuevo usuario 
-Eliminar usuario
-Actualizar contraseña o datos 
-Consultar información de usuario para inciio de sesión 

"""
load_dotenv()
variable = os.environ.get('OPENAI_KEY')
context = {"role": "system","content": "Eres un asistente muy útil."}
print("KEY ===== ")
print(variable)
messages = [context]
clientOpenAI = OpenAI(api_key= variable) 

def create_app(enviroment):
    app = Flask(__name__)
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
@app.route('/api/chatbot/users', methods =['POST'])
def create_user():
    if request.method == 'POST':
        data = request.json
        email = data.get('email')
        password = data.get('password')
        userName = data.get('username')
        userDB = db.user_collection.find_one({"email": email})
        if userDB:
            responsemessage = {"message": "El usuario no pudo ser creado exite una cuenta ya registrada con este correo electronico"}
            response = app.response_class(
                response=json.dumps(responsemessage),
                status=200,
                mimetype='application/json'
            )
            return response
        else:
            userDB = db.user_collection.insert_one({"email": email, "password": password, "username": userName})
            responsemessage = {"message": "El usuario fue creado de forma exitosa"}
            response = app.response_class(
                response=json.dumps(responsemessage),
                status=201,
                mimetype='application/json'
            )
            return response

@app.route('/userValidate', methods =['POST'])
def flask_mongodb_atlas():
    if request.method == 'POST':
        data = request.json
        email = data.get('email')
        userDB = db.user_collection.find_one({"email": email})
        if userDB:
            password = userDB.get('password')
            print(password)
            return "se encontro el usuario"
    return "flask mongodb atlas!"

@app.route("/test")
def test():
    db.user_collection.insert_one({"name": "New name"}).inserted_id
    return "Connected to the data base!"

# Ruta de gurdar dieta 
@app.route('/api/generate/diet', methods=['POST'])
def generateDiet():
    if request.method == 'POST':
        data = request.json
        email = data.get('email') 
        existDiet = db.diet_collection.find({"email": email})
        getDietList = list(existDiet)
        getDietNumber = len(getDietList)
        if(email == "sa337352@uaeh.edu.mx"):
            getDietNumber = 0
        print(getDietNumber)
        if getDietNumber > 5:
            print("No es posible generar una dieta " + email)
            responsemessage = {"message": "No fue posible generar una dieta, ya a utilizado esta función anteriormente", "response" : ""}
            response = app.response_class(
                response=json.dumps(responsemessage),
                status=200,
                mimetype='application/json'
            )
            return response
            ## Generar dieta, hacer petición
          
        else:
            print("Se va generar una dieta")
            prompt = data.get('prompt')
            print("Prompt")
            print(prompt)
            messages.append({"role": "user", "content": prompt})
            response = clientOpenAI.chat.completions.create(model="gpt-3.5-turbo", messages=messages)
            response_content = response.choices[0].message.content
            messages.append({"role": "assistant", "content": response_content})
            print(f"Respuesta: {response_content} | Fin ")
            response_diet = json.loads(response_content)

            print(f"DietJSON: {response_diet} | FIN")
            responsemessage = {"message": "Su dieta fue generada correctamente ", "data" : response_diet, "code": 201}
            print(responsemessage)
            response = app.response_class(
                response=json.dumps(responsemessage),
                status=201,
                mimetype='application/json'
            )
            return response
        
@app.route('/api/post/save/diet/user', methods=['POST'])
def saveDiet():
    print("Ruta para alamacenar dieta generada")
    if request.method == 'POST':
        data = request.json
        email = data.get('email')
        diet = data.get('diet')
        prompt = data.get('prompt')
        name = data.get('name')
        fecha_actual = datetime.now()
        fecha_string = fecha_actual.strftime("%d-%m-%Y")
        print("Se extrajeron los datos")
        documentToInsert = {"email": email, "diet": diet, "name": name, "prompt": prompt, "date": fecha_string}
        print(documentToInsert)
        db.diet_collection.insert_one(documentToInsert).inserted_id
        responsemessage = {"message": "Se guardo correctamente su dieta, puede consultarla más tarde si desea"}
        response = app.response_class(
            response=json.dumps(responsemessage),
            status=201,
            mimetype='application/json'
        )
        return response




#GET DIETAS POR USUARIO
@app.route('/api/getlist/diet', methods=['POST'])
def getDietList():
    print('Ruta para obtener lista de dietas por usuario')
    if request.method == 'POST':
        data = request.json
        email = data.get('email') 
        getDiet= db.diet_collection.find({"email" : email})
        print("getDiet:")
        print(getDiet)
        getDietList = list(getDiet)
        print("getDietList")
        print(getDietList)
        getDocumentsSize = len(list(getDietList))
        print("getDocumentsSize")
        print(getDocumentsSize)
        if(getDocumentsSize > 0):
            print("Se encontraron dietas para el usuario  " + email)
            dataJson = jsonfun.parse_json(getDietList)
            print(dataJson)
            responsemessage = {"message": "Se encontrarón las siguientes dietas", "data" : dataJson}
            response = app.response_class(
                response=json.dumps(responsemessage),
                status=201,
                mimetype='application/json'
            )
            return response
        else:
            print("No se encontraron dietas registradas anteriormente" )
            responsemessage = {"message": "No fue posible almacenar su comentario por favor intente más tarde", "data" : ""}
            response = app.response_class(
                response=json.dumps(responsemessage),
                status=200,
                mimetype='application/json'
            )
            return response



# POST COMENTARIOS
@app.route('/api/save/comment', methods=['POST'])
def saveComment():
    if request.method == 'POST':
        data = request.json
        email = data.get('email') 
        getDocumentsComment = db.comment_collection.find({"email" : email})
        getDocumentsSize = len(list(getDocumentsComment))
        print("respuesta: " )
        print( getDocumentsSize)
        if getDocumentsSize > 2:
            print("No fue posible almacenar comentario para  " + email)
            responsemessage = {"message": "No fue posible almacenar su comentario por favor intente más tarde", "response" : ""}
            response = app.response_class(
                response=json.dumps(responsemessage),
                status=200,
                mimetype='application/json'
            )
            return response
        else: 
            print("Proceso para almacenar documento ")
            comment = data.get('comment')
            title = data.get('title')
            print(comment)
            responsemessage = {"message": "Recibimos su comentario, muchas gracias por escribirnos", "response" : ""}
            documentToInsert = {"email": email, "title": title, "comment": comment}
            db.comment_collection.insert_one(documentToInsert).inserted_id
            response = app.response_class(
                response=json.dumps(responsemessage),
                status=201,
                mimetype='application/json'
            )
            return response
        

        
@app.route('/api/get/comment', methods=['POST'])
def getComments():
    if request.method == 'POST':
        data = request.json
        email = data.get('email') 
        getDocumentsComment = db.comment_collection.find({"email" : email})
        getDocumentsSize = len(list(getDocumentsComment))
        print("respuesta: " )
        print( getDocumentsSize)
        if getDocumentsSize > 2:
            print("No fue posible almacenar comentario para  " + email)
            responsemessage = {"message": "No fue posible almacenar su comentario por favor intente más tarde", "response" : getDocumentsComment}
            response = app.response_class(
                response=json.dumps(responsemessage),
                status=200,
                mimetype='application/json'
            )
            return response
        else:
            return "No se encontro nada "

            


if __name__ == '__main__':
    app.run(port=8000)