from flask import Flask
from markupsafe import escape

app = Flask(__name__)

@app.route('/')

def index():
    return 'Index Page'

@app.route('/about')
def hello():
    return 'Hola soy victoria y estudio ingenieria en desarrollo y gestion de software'