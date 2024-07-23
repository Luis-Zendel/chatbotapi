from __main__ import app
import json 

@app.route('/api/diets/test', methods = ['GET'])
def resolve():
    responsemesssage = {"message": "Hola mundo"}
    response = app.response_class(
        response=json.dumps(responsemessage),
        status=201,
        mimetype='application/json'
    )
    return response 