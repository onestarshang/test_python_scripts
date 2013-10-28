#coding = utf-8

import os,sys
import time

def test():
    _mydict = {}
    _vid_l = ['"93177"','"93173"','"93170"']
    file_list = ["data1","data2"]
    #_curp = os.path.curdir
    _curp = '.'

    count = 0
   
    for _file in file_list:
        f = open("%s/%s"%(_curp, _file))
        for _line in f:
            #if len(_line.split(':')) != 2:
            #    print _line
            
            if len(_line.split(':')) == 2 :
                _vid = _line.split(':')[0].strip()
                _keyl = _line.split(':')[1]
                #print _keyl
                if _vid not in _mydict : 
                    _mydict[_vid] = _keyl[2:].replace('],\r\r\n','')
                else:
                    _mydict[_vid] += ','+_keyl[2:].replace('],\r\r\n','')
                #print _mydict
                #count += 1
        f.close()
    
    fnew = open("%s/%s"%(_curp, "data_all"),'w+')
    fnew.write('{\r\r\n')
    for _k in _mydict : 
        fnew.write("%s%s%s%s%s"%(_k, ":", "[", _mydict[_k], "],\r\r\n"))
    fnew.write('}')
    fnew.close()
    
    
if __name__=='__main__':
    test()

