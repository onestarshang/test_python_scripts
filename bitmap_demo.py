#coding=utf-8

import os,sys
import time
import random

def create_num(num_count, rand_range_from, rand_range_to):
    #NUM = 100
    fp = 'num_file_%s.txt'%num_count
    f = open(fp, 'w')
    try:
        for i in range(num_count):
            _rn = '%s,'%str(random.randrange(rand_range_from,rand_range_to))
            f.write(_rn)
        f.close()
        return fp
    except Exception, e:
        print e

def bit_map(num_count, read_fp):
    _bm_list = {}
    for i in range(num_count):
        _bm_list[i]=0

    try:
        f = open(read_fp)
        _str = f.read()
        f.close()
        while(_str!=''):
            _t = int(_str[:_str.find(',')])
            _bm_list[_t] = 1
            _str = _str[_str.find(',')+1:]

        #print _bm_list

        f2 = open("sorted_num_%s.txt"%num_count,'w+')
        for _i in _bm_list:
            if _bm_list[_i]==1:
                _tstr = '%s,'%_i
                f2.write(_tstr)
        f2.close()

    except Exception, e:
        print e
    finally:
        f.close()
    #print len(_bm_list)


if __name__=='__main__':
    print "start create number file..."
    num_count = int(sys.argv[1])
    rand_range_from = int(sys.argv[2])
    rand_range_to = int(sys.argv[3])
    read_fp = create_num(num_count, rand_range_from, rand_range_to)
    print "create num file over!"
    time.sleep(2)
    stime = time.time()
    print "start to sort numbers in the file... time is : %.6f"%stime
    bit_map(num_count, read_fp)
    etime = time.time()
    _t = etime-stime
    print "end to sort numbers in the file...   total time is : %.6f"%_t
    print "end time is : %.6f"%etime
