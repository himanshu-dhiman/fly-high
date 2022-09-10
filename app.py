import os
from flask import Flask
from flask_restful import Api
from flask_cors import CORS
from src.resource.plan import Plan

app = Flask(__name__)

CORS(app)

api = Api(app)

api.add_resource(
    Plan,
    '/plan'
)

if __name__ == '__main__':
    app.run(debug = True)