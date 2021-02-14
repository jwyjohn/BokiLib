# -*- encoding: utf-8 -*-

from flask import Flask, Response, send_file
import flask_restful as restful
import hashlib
import dbm
from io import BytesIO
#from werkzeug.wsgi import FileWrapper
#from werkzeug import wrap_file
import os
import datetime

#init database

if not os.path.exists('/data/rawfile.dbm'):
    with dbm.open('/data/rawfile.dbm', 'n') as db:
        db['a0b65939670bc2c010f4d5d6a0b3e4e4590fb92b']='Hello World!\n'

if not os.path.exists('/data/filedate.dbm'):
    with dbm.open('/data/filedate.dbm', 'n') as db:
        db['a0b65939670bc2c010f4d5d6a0b3e4e4590fb92b']=str(datetime.datetime.now())

if not os.path.exists('/data/filesize.dbm'):
    with dbm.open('/data/filedate.dbm', 'n') as db:
        db['a0b65939670bc2c010f4d5d6a0b3e4e4590fb92b']='13'



app = Flask(__name__)
api = restful.Api(app)


class GetFileTime(restful.Resource):
    def get(self, sha1):
        res=''
        with dbm.open('/data/filedate.dbm', 'r') as db:
            try:
                res=db[sha1].decode(encoding="utf-8", errors="strict")
            except:
                return 'No such file.'

        return {'filedate':str(res)}

class GetFile(restful.Resource):
    def get(self, sha1):
        res_file=b''
        res_filename=str(datetime.datetime.now())
        with dbm.open('/data/rawfile.dbm', 'r') as db:
            try:
                res_file=db[sha1]
            except:
                return 'No such file.'
        b = BytesIO(res_file)
        response = Response(b, content_type='application/octet-stream')
        response.headers["Content-disposition"] = 'attachment; filename=%s' % res_filename  
        return response



api.add_resource(GetFileTime, '/t/<string:sha1>')
api.add_resource(GetFile, '/<string:sha1>')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
