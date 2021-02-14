# -*- encoding: utf-8 -*-

import hashlib
import dbm
from io import BytesIO
import os
import datetime
import time


def init_db(DATABASE_PATH='/data'):
    if not os.path.exists(DATABASE_PATH+'/rawfile.dbm'):
        with dbm.open(DATABASE_PATH+'/rawfile.dbm', 'n') as db:
            db['a0b65939670bc2c010f4d5d6a0b3e4e4590fb92b']='Hello World!\n'

    if not os.path.exists(DATABASE_PATH+'/filedate.dbm'):
        with dbm.open(DATABASE_PATH+'/filedate.dbm', 'n') as db:
            db['a0b65939670bc2c010f4d5d6a0b3e4e4590fb92b']=str(time.mktime(datetime.datetime.now().timetuple()))

    if not os.path.exists(DATABASE_PATH+'/filesize.dbm'):
        with dbm.open(DATABASE_PATH+'/filesize.dbm', 'n') as db:
            db['a0b65939670bc2c010f4d5d6a0b3e4e4590fb92b']='13'
    return 0

hex_nums='0123456789abcdef'

def check_sha1(s):
    if not len(s)==len('a0b65939670bc2c010f4d5d6a0b3e4e4590fb92b'):
        return False
    for ch in s:
        if ch not in hex_nums:
            return False
    return True


class BokiFileDB():
    """
    Database to store file in bokilib.
    Structure:  <hash>:<file bytes>
    Functions: hash2file,hash2date,hash2size,addfile
    """
    __DBPATH=''
    def __init__(self, DBPATH):
        self.__DBPATH=DBPATH
        init_db(self.__DBPATH)

    def hash2file(self, sha1):
        res_file=b''
        try:
            assert(check_sha1(sha1))
        except:
            return "Invalid hash."
        with dbm.open(self.__DBPATH+'/rawfile.dbm', 'r') as fdb:
            try:
                res_file=fdb[sha1]
            except:
                return 'No such file.'
        return res_file

    def hash2date(self, sha1):
        res_date=0
        try:
            assert(check_sha1(sha1))
        except:
            return "Invalid hash."
        with dbm.open(self.__DBPATH+'/filedate.dbm', 'r') as ddb:
            try:
                res_date=int(ddb[sha1])
            except:
                return 'No such file.'
        return res_date

    def hash2size(self, sha1):
        res_size=0
        try:
            assert(check_sha1(sha1))
        except:
            return "Invalid hash."
        with dbm.open(self.__DBPATH+'/filesize.dbm', 'r') as sdb:
            try:
                res_size=int(sdb[sha1])
            except:
                return 'No such file.'
        return res_size

    def addfile(self, rawfile):
        try:
            assert type(rawfile)==type(b'A')
            fsha1=hashlib.sha1(rawfile).hexdigest()
            ftime=str(time.mktime(datetime.datetime.now().timetuple()))
            fsize=str(len(rawfile))
            with dbm.open(self.__DBPATH+'/rawfile.dbm', 'r') as fdb:
                try:
                    fdb[fsha1]=rawfile
                except:
                    return 'Invalid FileDB'
            with dbm.open(self.__DBPATH+'/filedate.dbm', 'r') as ddb:
                try:
                    ddb[fsha1]=ftime
                except:
                    return 'Invalid Date'
            with dbm.open(self.__DBPATH+'/filesize.dbm', 'r') as sdb:
                try:
                    sdb[fsha1]=fsize
                except:
                    return 'Invalid Size'
        except:
            return 'Invalid File'
