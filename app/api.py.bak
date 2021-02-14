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

if not os.path.exists('/data/filename.dbm'):
    with dbm.open('/data/filename.dbm', 'n') as db:
        db['a0b65939670bc2c010f4d5d6a0b3e4e4590fb92b']='Hello_World.txt'

if not os.path.exists('/data/rawfile.dbm'):
    with dbm.open('/data/rawfile.dbm', 'n') as db:
        db['a0b65939670bc2c010f4d5d6a0b3e4e4590fb92b']='Hello World!\n'

if not os.path.exists('/data/filedate.dbm'):
    with dbm.open('/data/filedate.dbm', 'n') as db:
        db['a0b65939670bc2c010f4d5d6a0b3e4e4590fb92b']=str(datetime.datetime.now())

if not os.path.exists('/data/filesize.dbm'):
    with dbm.open('/data/filedate.dbm', 'n') as db:
        db['a0b65939670bc2c010f4d5d6a0b3e4e4590fb92b']='13'



print(dbm.whichdb('/data/filename.db'))



app = Flask(__name__)
api = restful.Api(app)



class HelloWorld(restful.Resource):
    def get(self):
        return {'hello': 'world'}
        #with dbm.open('/data/example.db', 'r') as db:
            #return str(db.keys())

class GetFileTime(restful.Resource):
    def get(self, sha1):
        res=''
        with dbm.open('/data/filedate.dbm', 'r') as db:
            try:
                res=db[sha1].decode(encoding="utf-8", errors="strict")
            except:
                return 'No such file.'

        return {'filedate':str(res)}



class GetFileName(restful.Resource):
    def get(self, sha1):
        res=''
        with dbm.open('/data/filename.dbm', 'r') as db:
            try:
                res=db[sha1].decode(encoding="utf-8", errors="strict")
            except:
                return 'No such file.'

        return {'filename':res}

class GetFile(restful.Resource):
    def get(self, sha1):
        res_file=b''
        res_filename=''
        with dbm.open('/data/rawfile.dbm', 'r') as db:
            try:
                res_file=db[sha1]
            except:
                return 'No such file.'
        b = BytesIO(res_file)
        #w = FileWrapper(b)
        #return Response(w, mimetype="text/plain", direct_passthrough=True)
        #return send_file(b, as_attachment=True, attachment_filename="testfile")
        with dbm.open('/data/filename.dbm', 'r') as db:
            try:
                res_filename=db[sha1].decode(encoding="utf-8", errors="strict")
            except:
                res_filename="404"


        #return send_file(b, attachment_filename=res_filename)
        response = Response(b, content_type='application/octet-stream')
        response.headers["Content-disposition"] = 'attachment; filename=%s' % res_filename  
        return response



api.add_resource(GetFileTime, '/t/<string:sha1>')
api.add_resource(GetFileName, '/n/<string:sha1>')
api.add_resource(GetFile, '/d/<string:sha1>')
api.add_resource(HelloWorld, '/')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
