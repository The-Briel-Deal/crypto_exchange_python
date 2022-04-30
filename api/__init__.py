from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
import os

db_url = os.getenv('DB_URL')

app = Flask(__name__)
CORS(app)
print(db_url)
app.config["SQLALCHEMY_DATABASE_URI"] = db_url
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)
@app.route('/')
def hello():
    return 'My First API !!'