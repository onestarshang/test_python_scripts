#coding = utf-8

import os, sys, time
import psycopg2
import simplejson

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
    
#--------------------------------------------------------------

asset_day = {
'20131001':[['1.1.1.1','1.1.1.2','1.1.1.3'],['1.1.1.4','1.1.1.5']],
'20131002':[['1.1.1.1','1.1.1.2','1.1.1.3'],['1.1.1.4','1.1.1.5']],
'20131003':[['1.1.1.1','1.1.1.2','1.1.1.3','1.1.1.4','1.1.1.5','1.1.1.6'],[]],
'20131004':[['1.1.1.1','1.1.1.2'],['1.1.1.3','1.1.1.4','1.1.1.5','1.1.1.6']],
'20131005':[['1.1.1.7'],['1.1.1.1','1.1.1.2','1.1.1.3','1.1.1.4','1.1.1.5','1.1.1.6']]
}

#intput data list
sorted_list = {'20131001':'4','20131002':'5','20131003':'6','20131004':'7'}
#sorted_list = {'20131001':'4','20131004':'7'}
#sorted_list = {'20131003':'4'}
#sorted_list = {'20131005':'6'}
#test data
ts_list = [
{'20131001':'4','20131002':'5','20131003':'6','20131004':'7'},
{'20131001':'4','20131004':'7'},
{'20131003':'4'},
{'20131005':'6'},
{'20131003':'4','20131005':'6'}
]
t_target = [
{'4':['1.1.1.2','1.1.1.5','1.1.1.7']},
{'5':['1.1.1.1','1.1.1.4']},
{'6':['1.1.1.4','1.1.1.5','1.1.1.6']},
{'7':['1.1.1.7']}
]

class RcmAssetRestat:
    ASSET_DB_NAME = 'rcm_stat_asset_'
    
    def __init__(self, slist):
        self._slist = slist
        self.stime = self._sort()[0]
        self.etime = '20131005'  #now time
        
    def __str__(self):
        return simplejson.dumps(self._slist)
    
    def get_input(self):
        return self._slist
    
    def _sort(self):
        sortt = sorted(self._slist, key=self._slist.get, reverse = False)
        return sortt
    
    def _t_s2i(self, tsrt):
        ti = time.mktime(time.strptime(tsrt,"%Y%m%d"))
        return int(ti)
    
    def _t_i2s(self, tint):
        ts = time.strftime("%Y%m%d",time.localtime(tint))
        return ts
    
    def get_stime(self):
        return self.stime
    
    def get_etime(self):
        return self.etime

    def allkeyl_fromdb(self, day_t):
        _kl = self.truekeyl_fromdb(day_t)
        _kl.extend(self.falsekeyl_fromdb(day_t))
        return _kl
    
    def truekeyl_fromdb(self, day_t):
        '''
        for test
        do sht fetch key list from DB
        sql = ''
        '''
        return asset_day[day_t][0]
    
    def falsekeyl_fromdb(self, day_t):
        '''
        for test
        do sht fetch key list from DB
        sql = ''
        '''
        return asset_day[day_t][1]
    
    def keyl_fromfile(self, tid):
        '''
        for test
        do sth find key list from files
        '''
        _tid = str(tid)
        for r in t_target:
            if r.has_key(_tid):
                _kl = r[_tid]
        return _kl

    def _intersec_keyl(self):
        pass
    
    def restat_keyl(self):
        sti = self._t_s2i(self.get_stime())
        eti = self._t_s2i(self.get_etime())
        inlist = self.get_input()
        sorttime = self._sort()
        s_i = 0
        e_i = 0
        tmp = []
        while sti<=eti:
            tstr = self._t_i2s(sti)
            if e_i == len(sorttime):
                e_i -= 1
#            print "s_i : %s"%s_i
#            print "e_i : %s"%e_i
            if sti == self._t_s2i(sorttime[s_i]):
                k_fromfile = self.keyl_fromfile(inlist[sorttime[s_i]])
                e_i += 1
                yield {tstr:k_fromfile}
            elif sti<self._t_s2i(sorttime[e_i]) and sti > self._t_s2i(sorttime[s_i]):
                k_fromfile = self.keyl_fromfile(inlist[sorttime[s_i]])
                falsek_indb = self.falsekeyl_fromdb(tstr)
                allk_indb = self.allkeyl_fromdb(tstr)
                res_r = set.intersection(set(k_fromfile), set(falsek_indb))
                res_d = set.difference(set(k_fromfile), set(allk_indb))
                res = set.union(res_r, res_d)
                yield {tstr:list(res)}
            elif sti == self._t_s2i(sorttime[e_i]):
                k_fromfile = self.keyl_fromfile(inlist[sorttime[e_i]])
                s_i += 1
                e_i += 1
                yield {tstr:k_fromfile}
            elif sti>self._t_s2i(sorttime[e_i]):
                k_fromfile = self.keyl_fromfile(inlist[sorttime[e_i]])
                falsek_indb = self.falsekeyl_fromdb(tstr)
                if tmp:
                    res = set.intersection(set(tmp), set(falsek_indb))
                else:
                    res = set.intersection(set(k_fromfile), set(falsek_indb))
                    tmp = list(res)
                yield {tstr:list(res)}
            sti += 86400
            
            

def test_restat_keyl():
    for sl in ts_list:
        rar = RcmAssetRestat(sl)
        print rar
        g_rar = rar.restat_keyl()
        while True:
            try:
                print g_rar.next()
            except StopIteration, e:
                print 'end'
                break
    pass


def test_attribut():
    rar = RcmAssetRestat(sorted_list)
    tt = '20131001'
    print "raw input list is : ", sorted_list
    print "print by json string : ", rar.get_input()
    print "sort input list by key : ", rar._sort()
    print "start time(origin by string) : ",rar.get_stime()
    si = rar._t_s2i(rar.get_stime())
    print "start time string to int : ",si
    print "start time int to string", rar._t_i2s(si)
    print "end time(origin by string) : ", rar.get_etime()
    ei = rar._t_s2i(rar.get_etime())
    print "end time string to int : ", ei
    print "end time int to string : ", rar._t_i2s(ei)
    print "%s allkeyl_fromdb : "%tt, rar.allkeyl_fromdb(tt)
    print "%s truekeyl_fromdb : "%tt, rar.truekeyl_fromdb(tt)
    print "%s falsekeyl_fromdb : "%tt, rar.falsekeyl_fromdb(tt)
    

if __name__=='__main__':
    test_attribut()
    test_restat_keyl()

    pass
