# coding=utf8


class ObjectCreator(type):

    def __new__(cls, clsname, bases, attrs):

        uppercase_attrs = {}
        print '********** attrs *********'
        print attrs
        for name, val in attrs.items():
            if not name.startswith('__'):
                uppercase_attrs[name.upper()] = val
            else:
                uppercase_attrs[name] = val
        return type.__new__(cls, clsname, bases, uppercase_attrs)


class TestCreator(dict):

    __metaclass__ = ObjectCreator

    def __init__(self, **kw):
        super(TestCreator, self).__init__(**kw)

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Dict' object has no attribute '%s'" % key)

    def __setattr__(self, key, value):
        self[key] = value

    def test(self):
        print 'test'

    @classmethod
    def haha(cls):
        print 'haha'



tc = TestCreator(test='1', test2='2')
print tc
print hasattr(TestCreator, 'test')

TestCreator.HAHA()



'''
output:

$ python test_classes.py
********** attrs *********
{'__module__': '__main__', '__metaclass__': <class '__main__.ObjectCreator'>, 'haha': <classmethod object at 0x10b228c90>, '__setattr__': <function __setattr__ at 0x10b226d70>, '__getattr__': <function __getattr__ at 0x10b226cf8>, 'test': <function test at 0x10b226de8>, '__init__': <function __init__ at 0x10b226c80>}
{'test': '1', 'test2': '2'}
False
haha
'''



###  __call__



class Entity(object):
    '''表示一个实体的类，调用它的实例
       可以更新实体的位置'''

    def __init__(self, size, x, y):
        self.x, self.y = x, y
        self.size = size

    def __call__(self, x, y):
        '''改变实体的位置'''
        print '__call__'
        self.x, self.y = x, y


e = Entity(1, 2, 3)
print e.x, e.y

e(1, 2)

print e.x, e.y

'''
2 3
__call__
1 2


魔法方法：

http://pyzh.readthedocs.io/en/latest/python-magic-methods-guide.html
'''
