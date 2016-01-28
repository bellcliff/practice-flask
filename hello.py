import os
from flask import Flask, send_file

BASE_DIR = os.path.dirname(os.path.realpath(__file__))
app = Flask(__name__)

@app.route("/")
def hello():
    return send_file(BASE_DIR + '/static/index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8090, debug=True)
