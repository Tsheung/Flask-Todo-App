from flask import flask

app = Flask(__name__)

def index():
    return "Hello World"