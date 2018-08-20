from flask import Flask

app = Flask(__name__)

from app import routes, routes2, routes3, routes4
