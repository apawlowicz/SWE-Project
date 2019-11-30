from flask import Flask, request
from flask_cors import CORS, cross_origin
from flask_restful import Resource, Api
from json import dumps
from flask_jsonpify import jsonify
import sys

sys.path.insert(1, 'analysis')
from frequencies import getFrequencies

app = Flask(__name__)
api = Api(app)

CORS(app)

@app.route("/")
def hello():
    return jsonify({'text':'Hello World!'})

class Employees(Resource):
    def get(self):
        return {'employees': [{'id':1, 'name':'Balram'},{'id':2, 'name':'Tom'}]} 

class Employees_Name(Resource):
    def get(self, file):
        return jsonify(getFrequencies(file))       


api.add_resource(Employees, '/employees') # Route_1
api.add_resource(Employees_Name, '/employees/<file>') # Route_3


if __name__ == '__main__':
   app.run(port=5002)
