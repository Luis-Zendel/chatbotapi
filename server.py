import os
import json 
from flask import Flask, render_template, request, redirect
from flask import jsonify
from config import config
from openai import OpenAI
from dotenv import load_dotenv
from flask_cors import CORS
from flask_pymongo import pymongo


load_dotenv()
MONGO_URI = os.getenv('MONGO_URI')

clientM = pymongo.MongoClient("mongodb+srv://ron_dev:xpLWZNrY0wunNO9n@components.xh8te5c.mongodb.net/?retryWrites=true&w=majority")
db = clientM.get_database('nutritionapp')
user_collection = pymongo.collection.Collection(db, 'users')

KEY = os.getenv('URL_OPENAI_KEY')


client = OpenAI(api_key=KEY) 

context = {"role": "system","content": "Eres un asistente muy útil."}
messages = [context]

def separar_horario(plan_alimenticio, horario, siguiente_horario):
    # Encontrar el índice del horario en el plan alimenticio
    indice_horario = plan_alimenticio.find(horario)
    print("Se encontro indice horario", indice_horario)
    # Si el horario no se encuentra, retornar None
    if indice_horario == -1:
        return None

    # Encontrar el inicio del contenido del horario (línea siguiente al horario)
    inicio_contenido = plan_alimenticio.find('\n', indice_horario) + 1

    # Encontrar el final del contenido del horario (inicio del siguiente horario o el final de la cadena)

    fin_contenido = plan_alimenticio.find(siguiente_horario) 
    print("Fin de contenido ", fin_contenido)
    # Extraer el contenido del horario
    if siguiente_horario != "":
        contenido_horario = plan_alimenticio[inicio_contenido:fin_contenido].strip()
    else:
        contenido_horario = plan_alimenticio[inicio_contenido:].strip()

    return contenido_horario

def create_app(enviroment):
    app = Flask(__name__)
    CORS(app)
    app.config.from_object(enviroment)
    return app

enviroment = config['development']
app = create_app(enviroment)

@app.route("/api/nutritionbot/users", methods=['GET'])
def test():
    if request.method == 'GET':
        user_collection.insert_one({"name": "John"})
        db.db.collection.insert_one({"name": "John"})
        return jsonify({'message' : "Connected to the data base!"})

@app.route('/api/nutrition/chatbot', methods=['POST', 'GET'])
def get_conversation():
    response2 = {'message': 'success'}
    if request.method == 'POST':
        body = request.json
        print(body.get('name'))
        content = body.get('name')
        messages.append({"role": "user", "content": content})
        response = client.chat.completions.create(model="gpt-3.5-turbo", messages=messages)
        response_content = response.choices[0].message.content
        messages.append({"role": "assistant", "content": response_content})
        print(f"[bold green]> [/bold green] [green]{response_content}[/green]")
        desayuno = separar_horario(response_content, "Desayuno:", "Media mañana:")
        media_manana = separar_horario(response_content, "Media mañana:",  "Almuerzo:")
        almuerzo = separar_horario(response_content, "Almuerzo:", "Media tarde:")
        media_tarde = separar_horario(response_content, "Media tarde:",  "Cena:")
        cena = separar_horario(response_content, "Cena:", "Antes de dormir:")
        antes_de_dormir = separar_horario(response_content, "Antes de dormir:", "")
        response_diet = {
            'desayuno': desayuno,
            'media_manana': media_manana,
            'almuerzo': almuerzo,
            'media_tarde': media_tarde,
            'cena': cena,
            'antes_de_dormir': antes_de_dormir
        }
        return jsonify(response_diet)
    if request.method == 'GET':
        return jsonify(response2)

if __name__ == '__main__':
    app.run(debug=True)