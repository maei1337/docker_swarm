from flask import Flask
from flask_restful import Resource, Api
import requests

app = Flask(__name__)
api = Api(app)

url = "http://service_2:5002/"

class HelloWorld(Resource):
    def get(self):
        response = requests.request("GET", url)
        return {'hello': response.text}

api.add_resource(HelloWorld, '/')

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5001)