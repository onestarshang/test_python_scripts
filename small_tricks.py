#coding:utf-8

"""
字典按值排序
"""
import operator

res = {'a':2, 'b':1}
sorted_res = sorted(res.iteritems(), key=operator.itemgetter(1))


"""
时间转换
"""
def _t_s2i(tsrt):
    ti = time.mktime(time.strptime(tsrt,"%Y%m%d"))
    return int(ti)
    
def _t_i2s(tint):
    ts = time.strftime("%Y%m%d",time.localtime(tint))
    return ts

if __name__ == '__main__':
	pass