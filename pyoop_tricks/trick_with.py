# -*- encoding:utf-8 -*-

"""
eg 1 :
"""
class Sample1:
	def __enter__(self):
		print "In __enter__()"
		return "Foo"

	def __exit__(self, type, value, trace):
		print "In __exit__()"

def get_sample():
	return Sample1()

with get_sample() as sample:
	print "sample:", sample

"""
result ==== :

In __enter__()
sample: Foo
In __exit__()
"""

"""
eg 2 :
"""

class Sample2:
    def __enter__(self):
        return self
 
    def __exit__(self, type, value, trace):
        print "type:", type
        print "value:", value
        print "trace:", trace
 
    def do_something(self):
        bar = 1/0
        return bar + 10
 
with Sample2() as sample:
    sample.do_something()



"""
这看起来充满魔法，但不仅仅是魔法，Python对with的处理还很聪明。
基本思想是with所求值的对象必须有一个__enter__()方法，一个__exit__()方法。

紧跟with后面的语句被求值后，返回对象的__enter__()方法被调用，
这个方法的返回值将被赋值给as后面的变量。当with后面的代码块全部被执行完之后，
将调用前面返回对象的__exit__()方法。


1. __enter__()方法被执行
2. __enter__()方法返回的值 - 这个例子中是"Foo"，赋值给变量'sample'
3. 执行代码块，打印变量"sample"的值为 "Foo"
4. __exit__()方法被调用
with真正强大之处是它可以处理异常。
可能你已经注意到Sample类的__exit__方法有三个参数- val, type 和 trace。 
这些参数在异常处理中相当有用。我们来改一下代码，看看具体如何工作的。

"""


"""
eg 3:

Using these magic methods (__enter__, __exit__) allows you to implement objects 
which can be used easily with the with statement.

The general idea is that it makes it easy to build code which needs some 'cleandown' 
code executed (think of it as a try-finally block). Some more explanation here.

A useful example could be a database connection object (which then automagically 
	closes the connection once the corresponding 'with'-statement goes out of scope:
"""
class DatabaseConnection(object):

    def __enter__(self):
        # make a database connection and return it
        return self.dbconn

    def __exit__(self, type, value, tb):
        # make sure the dbconnection gets closed
        self.dbconn.close()

import pymongo

class MongoDB(object):
    
    def __init__(self):
        self.conn = pymongo.Connection('127.0.0.1', 27017)
        self.mongo_db = self.conn['yourdbname']
    
    def __enter__(self):
        return self.mongo_db
    
    def __exit__(self, exc_type, exc_value, traceback):
        self.conn.disconnect()


with MongoDB as mongodb:
	res = mongodb['yourcollectionname'].find({})