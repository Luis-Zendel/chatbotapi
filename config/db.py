from flask import Flask
from flask_pymongo import pymongo

CONNECTION_STRING = "mongodb+srv://mr_robot:1234$@components.xh8te5c.mongodb.net/?retryWrites=true&w=majority"
client = pymongo.MongoClient(CONNECTION_STRING)
db = client.nutritionapp
# Colección de usuario de mongo atlas 
user_collection = client.nutritionapp.users


class Config:
    MONGO_URI = "mongodb+srv://mr_robot:1234$@components.xh8te5c.mongodb.net/?retryWrites=true&w=majority"
