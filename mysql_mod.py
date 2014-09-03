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


class MysqlDBExecutor(object):

    def __init__(self, serverhost, dbname, username, password, charset='utf8'):
        self.conn = mdb.connect(serverhost, username, password, dbname, charset = charset)
        self.curs = self.conn.cursor()

    def __enter__(self):
        return self.__rundb

    def __rundb(self, sql, vals=[] , db_conf={}, result=True):
        self.curs.execute(sql , vals)
        self.conn.commit()
        r = None
        if result :
            r = self.curs.fetchall()
        return r

    def __exit__(self, exc_type, exc_value, traceback):
        try:
            self.curs.close()
        except Exception, e:
            logging.error(e)

        try:
            self.conn.close()
        except Exception, e:
            logging.error(e)


if __name__ == '__main__':
    #tt = "select * from tag_users where name like '%%"+name+"%%'"

    tt2 = """....."""

    res = rundb(tt2, [xxx])
    print res
    with MysqlDBExecutor(HOST, DB, UID, PWD) as execdb:
        sql = """select id from mysites_vultask limit 3;"""
        res = execdb(sql)
        print res

    pass