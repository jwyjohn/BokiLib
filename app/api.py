# -*- encoding: utf-8 -*-

from flask import Flask
import flask_restful as restful
import hashlib
import dbm


with dbm.open('/data/example.db', 'n') as db:
    db['key'] = 'value'
    db['today'] = 'Sunday'
    db['author'] = 'Doug'

print(dbm.whichdb('/data/example.db'))



app = Flask(__name__)
api = restful.Api(app)



class HelloWorld(restful.Resource):
    def get(self):
        #return {'hello': 'world'}
        with dbm.open('/data/example.db', 'r') as db:
            return str(db.keys())

api.add_resource(HelloWorld, '/')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
