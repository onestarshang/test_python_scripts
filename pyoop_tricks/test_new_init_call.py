# -*- encoding:utf-8 -*-


# class Singleton(type):
#     def __init__(self, *args, **kwargs):
#         super(Singleton, self).__init__(*args, **kwargs)
#         self.__instance = None

#     def __call__(self, *args, **kwargs):
#         print '__call__'
#         if self.__instance is None:
#             print '__call__ once'
#             self.__instance = super(Singleton, self).__call__(*args, **kwargs)
#         return self.__instance


# s1 = Singleton(1)
# s2 = Singleton('str')
# s3 = Singleton(2.5)
# print s1
# print s2
# print s3



class A(object):
    _dict = {}

    def __new__(cls):
        print 'into __new__'
        print cls
        if 'key' in A._dict:
            print 'EXIST'
            print A._dict['key']
            return A._dict['key']
        else:
            print '__new__'
            return super(A, cls).__new__(cls)

    def __init__(self):
        print '__init__'
        print self
        A._dict['key'] = self

    def __call__(self, *args, **kwargs):
        print '__call__'
        print self
        print args
        print kwargs


a1 = A()
print '=============='
a2 = A()
a2([1,2,3], test=1)
print '=============='
# print a2
# a3 = A()

"""
into __new__
__new__
__init__
==============
into __new__
EXIST
__init__
==============
into __new__
EXIST
__init__
"""


def singleton(cls):
    instances = {}
    def getinstance(a):
        if cls not in instances:
            instances[cls] = cls(a)
        return instances[cls]
    return getinstance

@singleton
class A:

    def __init__(self, a):
        print a
        pass

aa1 = A(1)
# aa2 = A(2)
print aa1
# print aa2


class Singleton(object):
    _instance = None
    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(Singleton, cls).__new__(
                                cls, *args, **kwargs)
        return cls._instance

    def __init__(self, *args, **kwargs):
        print args
        print kwargs



s1 = Singleton(1, {1:3}, ['ddddd'], 'd', test=1, test2=2)
s2 = Singleton([2])

# print s1
# print s2


class Singleton(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]

#Python2
# class MyClass(BaseClass):
#     __metaclass__ = Singleton
