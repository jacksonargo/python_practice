import requests  # https://requests.readthedocs.io/en/latest/user/quickstart/
from flask import Flask  # https://flask.palletsprojects.com/en/1.1.x/quickstart/#quickstart

app = Flask(__name__)


@app.route('/cup')
def home():
    return requests.get("https://foaas.com/cup/jackson", headers={"Accept": "application/json"}).text, \
           200, {"Content-Type": "application/json"}
