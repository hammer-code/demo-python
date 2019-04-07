from flask import Flask, jsonify, request
import json
import random
from flask_cors import CORS
from db_factory import create_user_db

app = Flask(__name__)
CORS(app)

user_db = create_user_db()

@app.route("/users", methods=["GET"])
def getUsers():
    return jsonify({
        'users': user_db.all()
    })

@app.route("/users", methods=["POST"])
def addUser():
    body = json.loads(request.data)

    user = {
        'id': str(random.random()),
        'name': body['name']
    }

    user_db.add(user)

    return jsonify({
        'user': user
    })

@app.route("/users/<id>", methods=["DELETE"])
def removeUser(id):
    user_db.remove(id)

    return jsonify({
        'message': 'User been deleted'
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=4000)
