import os
from flask import Flask, send_file, Response
from pymongo import MongoClient
from bson.json_util import dumps

BASE_DIR = os.path.dirname(os.path.realpath(__file__))
app = Flask(__name__)

db = MongoClient('mongodb://localhost:27017').test

@app.route("/")
def hello():
    return send_file(BASE_DIR + '/static/index.html')

@app.route('/api/user', methods=['GET'])
def list():
    users = dumps(db.customers.find())
    resp = Response(users, mimetype='application/json')
    return resp

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8090, debug=True)
