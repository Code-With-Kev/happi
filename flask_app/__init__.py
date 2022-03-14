from flask import Flask, session
from flask_bcrypt import Bcrypt

app = Flask(__name__)
app.secret_key = "root"

bcrypt = Bcrypt(app)

DB = "painting_schema"