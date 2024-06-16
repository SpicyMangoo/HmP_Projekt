from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS


app = Flask(__name__)

# ALLOW CORS FOR ALL ROUTES 
CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://USER437521:HackingMitPython@spicymango.lima-db.de:3306/db_437521_1'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'f1c50cdf58a5ac7024799454'

db = SQLAlchemy(app)

from taskmanager import routes
