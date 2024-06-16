from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://USER437521:HackingMitPython@spicymango.lima-db.de:3306/db_437521_1'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'f1c50cdf58a5ac7024799454'

db = SQLAlchemy(app)

from taskmanager import routes
