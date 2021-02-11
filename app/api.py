# -*- encoding: utf-8 -*-

from flask import Flask
import flask_restful as restful

app = Flask(__name__)
api = restful.Api(app)

class HelloWorld(restful.Resource):
    def get(self):
        return {'hello': 'world'}

api.add_resource(HelloWorld, '/')

if __name__ == '__main__':
    #app.run(debug=True)
    app.run(debug=True, host='0.0.0.0')
