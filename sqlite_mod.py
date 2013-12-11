#coding:utf-8
import sys, os, time
import sqlite3

class SqliteMod:
    
    def __init__(self, dbpath, mod = None):
        if not mod:
            self.dbpath = dbpath
            self.conn = sqlite3.connect(self.dbpath)
            self.cur = self.conn.cursor()
        elif mod == 'memory':
            self.conn = sqlite3.connect(":memory:")
            self.cur = self.conn.cursor()
    
    def __str__(self):
        return self.dbpath
    
    def _getCur(self):
        return self.cur
    
    def rundb(self, sql, vals = [], result=True):
        try :
            self.cur.execute(sql , vals)
            self.conn.commit()
            r = None
            if result :
                r = self.cur.fetchall()
            return r
        except BaseException , e :
            print e
            print sql
            self.conn.close()
            r = None
    
    def disconn(self):
        self.conn.close()
    
    
if __name__ == "__main__":
    sm = SqliteMod('test.DB')
#    print sm._getCur()
#    print sm
##    sm.rundb("""create table dbfrd(dbid,link,img);""")
#    testdata = [['wtforz', 'http://www.douban.com/people/wtforz', 'http://img3.douban.com/icon/ul2063361-7.jpg'],
#                ['hinabook', 'http://www.douban.com/people/hinabook', 'http://img3.douban.com/icon/ul2989625-8.jpg'],
#                ['aaaaaaaaaaa', 'http://www.douban.com/people/aaaaaaaaaaa', 'http://img3.douban.com/icon/ul48329159-56.jpg']
#                ]
#    for dd in testdata:
#        sm.rundb('insert into dbfrd(dbid, link, img) values(?,?,?);', dd)
    res = sm.rundb('select * from dbfrd;')
    for i in res : 
        print i
    cnt = sm.rundb('select count(*) from dbfrd;')
    print cnt
    ord = sm.rundb('select dbid from dbfrd order by dbid')
    print ord
    sm.disconn()
