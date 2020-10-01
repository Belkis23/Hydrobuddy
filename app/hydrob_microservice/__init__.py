import os
from flask import Flask, redirect, url_for, request, render_template
from pymongo import MongoClient
from flask_mongoalchemy import MongoAlchemy
from flask_marshmallow import Marshmallow
from flask_bcrypt import Bcrypt
from flask_cors import CORS,cross_origin

from flask_hashing import Hashing


app = Flask(__name__)

# #client = MongoClient(os.environ['DB_PORT_27017_TCP_ADDR'],27017)
# client = MongoClient('mongodb://db:27017/')
# db = client.tododb
# db = client.PointOfSale_DB

CORS(app,supports_credentials=True)
app.config['CORS_HEADERS'] = "content-type"
app.config['CORS_RESOURCES'] = {r"/*": {"origins": "*"}}

app.config['MONGOALCHEMY_DATABASE'] = 'Hydrob_DB'
app.config['MONGOALCHEMY_CONNECTION_STRING'] = 'mongodb://db:27017/'
app.config['MONGOALCHEMY_ECHO'] = True
db = MongoAlchemy(app)

# Init marshmallow
ma = Marshmallow(app)



from hydrob_microservice.formulations.routes import pos
app.register_blueprint(pos)



