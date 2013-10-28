#coding=utf-8

import sys,os,time
from lxml import etree as le

class Str2xml:
    
    def __init__(self, in_path, encoding='utf-8'):
        """
        test
        """
        self.context = le.iterparse(in_path)
        self._in_path = in_path
        
    def get_context(self):
        return self.context
    
    def get_node_by_tag(self, tag):
        reload(sys)
        sys.setdefaultencoding('utf8')
        
        sx = self.get_context()
        try:
            for _end, _el in sx:
                if _el.tag == tag:
                    yield _el
        except BaseException, e:
            print 'error...'
            print le.tostring(_el.getprevious())

 
class RawStr2xml:
    
    def __init__(self, in_path):
        self.node = ''
        self._in_path = in_path
        self._f_handler = open(self._in_path)
        
    def _repr(self):
        for l in self._f_handler:
            print l
            print type(l)
#        print self._f_handler
        
    def get_node_by_tag(self, tag):
        node = ''
        _is_save = False
        while True:
            try:
                _line = self._f_handler.next()
                if _line.find('<%s>'%tag) != -1:
                    node = ''
                    _is_save = True
                if _is_save:
                    node += _line
                if _line.find('</%s>'%tag) != -1:
                    yield node
                    _is_save = False
                    continue
            except StopIteration:
                print 'parse %s nodes end...'%tag
                self._f_handler.close()
                break
  
    
if __name__=='__main__':
#    sx = Str2xml(sys.argv[1])
    sx = RawStr2xml('test.xml')
    node_iterator = sx.get_node_by_tag('INFO')
    print node_iterator.next()
    time.sleep(2)
    while True:
        try:
            cur_node = node_iterator.next()
            #do sth with cur_node
#            print cur_node
#            while cur_node.getprevious() is not None:
#                del cur_node.getparent()[0]
        except StopIteration, e:
            print 'end'
            break
    print 'test'
