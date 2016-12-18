from flask import Flask
from . secret import secret_key

app = Flask(__name__)
app.config["SECRET_KEY"] = secret_key

from bs_app import views
