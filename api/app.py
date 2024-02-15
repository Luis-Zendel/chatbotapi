from flask import Flask, render_template, request, redirect
from flask_pymongo import pymongo
from flask import jsonify
import json 
import db
CONNECTION_STRING = "mongodb+srv://mr_robot:1234$@components.xh8te5c.mongodb.net/?retryWrites=true&w=majority"
client = pymongo.MongoClient(CONNECTION_STRING)




app = Flask(__name__)
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


if __name__ == '__main__':
    app.run(port=8000)