# -*- encoding: utf-8 -*-

from flask import Flask, Response, send_file
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
api = restful.Api(app)


class GetFileInfo(restful.Resource):
    def get(self, sha1):
        res=boki_db.hash2date(sha1)
        return {'filedate':res}


class GetFile(restful.Resource):
    def get(self, sha1):
        res_file=boki_db.hash2file(sha1)
        if not type(res_file)==type(b'A'):
            return "No such file."
        res_filename=str(int(time.mktime(datetime.datetime.now().timetuple())))
        b = BytesIO(res_file)
        response = Response(b, content_type='application/octet-stream')
        response.headers["Content-disposition"] = 'attachment; filename=%s' % res_filename
        return response



api.add_resource(GetFileInfo, '/i/<string:sha1>')
api.add_resource(GetFile, '/<string:sha1>')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
