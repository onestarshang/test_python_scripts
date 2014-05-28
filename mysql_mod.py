#coding:utf-8

import MySQLdb as mdb 
import sys


DB = ''
HOST = ''
UID = ''
PWD = ''
PORT_NUM = 0
CHARCODE = 'utf8'

#test_db
#--------------------------------------------------------------
def connectdb():
    _db = DB
    _host = HOST
    _port = PORT_NUM
    _uid = UID
    _pwd = PWD
    _charcode = CHARCODE
    #连接mysql的方法：connect('ip','user','password','dbname')
    conn =  mdb.connect(_host, _uid, _pwd, _db, charset=_charcode)
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

if __name__ == '__main__':
    #tt = "select * from tag_users where name like '%%"+name+"%%'"

    tt2 = """....."""

    res = rundb(tt2, [xxx])
    print res