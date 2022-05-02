from flask import Flask
from flask_sqlalchemy import SQLAlchemy

api = Flask(__name__, static_folder='../build', static_url_path='/')
api.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///forests.sqlite3'
db = SQLAlchemy(api)

if __name__ == '__main__':
    from views import *
    from models import init
    init()
    api.run(debug=True)