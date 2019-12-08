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
class frequencyList(Resource):
    def get(self, file):
        print(file)
        return jsonify(getFrequencies(file))       


api.add_resource(frequencyList, '/frequencies/<file>')


if __name__ == '__main__':
   app.run(port=5002)
