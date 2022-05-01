from flask import Flask
from flask_sqlalchemy import SQLAlchemy

api = Flask(__name__)
api.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///forests.sqlite3'
db = SQLAlchemy(api)

print(__name__)

if __name__ == '__main__':
    from views import *
    from models import init
    init()
    api.run(debug=True)