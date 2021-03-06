# -*- encoding: utf-8 -*-

from flask import Flask, Response, send_file, request, abort
from flask_restful import reqparse, Resource, Api
import flask_restful as restful
import hashlib
from io import BytesIO
#from werkzeug.wsgi import FileWrapper
#from werkzeug import wrap_file
import os
import datetime
from boki_db import *
#init database
boki_db=BokiFileDB("../data")

app = Flask(__name__)
api = Api(app)


class GetFileInfo(Resource):
    def get(self, sha1):
        return {'hash':sha1,'size':boki_db.hash2size(sha1),'date':boki_db.hash2date(sha1)}


class GetFile(Resource):
    def get(self, sha1):
        res_file=boki_db.hash2file(sha1)
        if not type(res_file)==type(b'A'):
            #abort(404)
            return 404
        res_filename=str(int(time.mktime(datetime.datetime.now().timetuple())))
        b = BytesIO(res_file)
        response = Response(b, content_type='application/octet-stream')
        response.headers["Content-disposition"] = 'attachment; filename=%s' % res_filename
        return response

class UploadFile(Resource):
    def post(self):
        file = request.files['file']
        file_bytes = file.read()
        add_res=boki_db.addfile(file_bytes)
        if check_sha1(add_res):
            return add_res
        else:
            #abort(401)
            return 404


api.add_resource(GetFileInfo, '/i/<string:sha1>')
api.add_resource(GetFile, '/<string:sha1>')
api.add_resource(UploadFile, '/u')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
