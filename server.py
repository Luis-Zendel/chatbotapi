import os
from flask import Flask, render_template, request, redirect
from flask import jsonify
from config import config
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
KEY = os.getenv('URL_OPENAI_KEY')


client = OpenAI(api_key=KEY) 

context = {"role": "system","content": "Eres un asistente muy útil."}
messages = [context]

def create_app(enviroment):
    app = Flask(__name__)
    app.config.from_object(enviroment)
    return app

enviroment = config['development']
app = create_app(enviroment)

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

        return jsonify(response_content)
    if request.method == 'GET':
        return jsonify(response2)

if __name__ == '__main__':
    app.run(debug=True)