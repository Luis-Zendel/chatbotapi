from flask import Flask
from flask_pymongo import pymongo

CONNECTION_STRING = "mongodb+srv://mr_robot:1234$@components.xh8te5c.mongodb.net/?retryWrites=true&w=majority"
client = pymongo.MongoClient(CONNECTION_STRING)
db = client.nutritionapp
user_collection = client.nutritionapp.users
diet_collection = client.nutritionapp.diet_collection
comment_collection = client.nutritionapp.comment_collection

response = diet_collection.find({"email" : "sa337352@uaeh.edu.m"})
print("respuesta: " )
print( len(list(response)))
"""
tam = response.count()
print("Tamaño = " + tam)
for document in response:
    print(document)

"""