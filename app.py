import os
from flask import Flask
from flask_restful import Api
from src.resource.plan import Plan

app = Flask(__name__)

api = Api(app)

api.add_resource(
    Plan,
    '/plan'
)

if __name__ == '__main__':
    app.run(debug = True)