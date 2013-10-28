#coding = utf-8

import os, sys, time
import psycopg2

DB = ''
HOST = ''
UID = ''
PWD = ''
PORT_NUM = 0

#test_db
#--------------------------------------------------------------
def connectdb():
    _db = DB
    _host = HOST
    _port = PORT_NUM
    _uid = UID
    _pwd = PWD
    _connstr = 'dbname=%s host=%s port=%s user=%s password=%s'
    _connstr = _connstr % (_db,_host,_port,_uid,_pwd)
    conn = psycopg2.connect(_connstr)
    curs = conn.cursor()
    return curs , conn
    
def disconnectdb(_curs,_conn):
    try :
        _curs.close()
    except BaseException , e :
        pass
    
    try :
        _conn.close()
    except BaseException , e :
        pass

def rundb(sql, vals=[] , db_conf={}, result=True):
    try :
        curs , conn = connectdb()
        curs.execute(sql , vals)
        conn.commit()
        r = None
        if result :
            r = curs.fetchall()
        return r
    except BaseException , e :
        print e
        print sql
        r = None
    finally:
        disconnectdb(curs, conn)
        return r


if __name__=='__main__':
    #print rundb('select * from test where id=%s',[1])
    pass
