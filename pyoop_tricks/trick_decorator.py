# -*- encoding:utf-8 -*-


"""

def printdebug(func):
	def __decorator():
		print('enter the login')
		func()
		print('exit the login')
	return __decorator

@printdebug
def login():
    print('in login')

login()
"""




"""
eg 2 : 装饰有返回值的函数

==============================================================================
调用顺序:

...omit for brief…[real][msg from login(‘jatsz’) => 
[result from]__decorator => [assign to] result1

==============================================================================


def printdebug(func):
	def __decorator(user):
		print('enter the login')
		result = func(user)#recevie the native function call result
		print('exit the login')
		return result#return to caller
	return __decorator

@printdebug
def login(user):
	print('in login:' + user)
	msg = "success" if user == "jatsz" else "fail"
	return msg#login with a return value

result1 = login('jatsz')
print result1#print login result

result2 = login('candy')
print result2


eg 3 : 装饰器本身有参数

==============================================================================
调用顺序:

[decorated]login(‘jatsz’) => printdebug_level(5) => 
printdebug[with closure value 5](login)(‘jatsz’) => 
__decorator(‘jatsz’)[use value 5]  => [real]login(‘jatsz’)



==============================================================================
dir(__decorator) : 

<function __decorator at 0x017B6BB0>
['__call__', '__class__', '__closure__', '__code__', '__defaults__', '__delattr__', 
'__dict__', '__doc__', '__format__', '__get__', '__getattribute__', '__globals__', 
'__hash__', '__init__', '__module__', '__name__', '__new__', '__reduce__', 
'__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', 
'__subclasshook__', 'func_closure', 'func_code', 'func_defaults', 'func_dict', 'func_doc', 
'func_globals', 'func_name']


# import dis

def printdebug_level(level):#add wrapper to recevie decorator's parameter
    def printdebug(func):
    	def __decorator(user):
    	    print('enter the login, and debug level is: ' + str(level))#print debug level
    	    func(user)
    	    print('exit the login')
    	# print '================'
    	# 这部分是闭包的功能
    	# print __decorator
    	# print type(__decorator.func_code)
    	# print __decorator.func_closure
    	# print __decorator.func_code
    	# dis.dis(__decorator.func_code)

    	# print '================'
    	return __decorator
    return printdebug #return original decorator

@printdebug_level(level=5)#decorator's parameter, debug level set to 5
def login(user):
	print('in login:' + user)

login('jatsz')


eg 4 : 应用多个装饰器

==============================================================================
调用顺序:

[printdebug decorated]logout() =>
printdebug.__decorator[call [others decorated]logout() ] =>
printdebug.__decorator.other.__decorator[call real logout]



out : 

$ python deoc.py
***other decorator***
enter the login
in login:
exit the login
---------------------------
enter the login
***other decorator***
in logout:
exit the login




def printdebug(func):
	def __decorator():
		print('enter the login')
		func()
		print('exit the login')
	return __decorator


def others(func):#define a other decorator
    def __decorator():
    	print '***other decorator***'
    	func()
    return __decorator


@others#apply two of decorator
@printdebug
def login():
	print('in login:')


@printdebug#switch decorator order
@others
def logout():
	print('in logout:')

login()
print('---------------------------') 
logout()


"""



"""
PRACTICE:


来个更加真实的应用，有时候validate是个耗时的过程。为了提高应用的性能，
我们会将validate的结果cache一段时间(30 seconds)，借助decorator和上面的方法，
我们可以这样实现：


==============================================================================


"""
import time
dictcache = {}
def cache(func):
	print 'cache.....'
	def __decorator(user):
		now = time.time()
		if user in dictcache:
			result, cache_time = dictcache[user]
			if (now - cache_time) > 30:#cache expired
			    result = func(user)
			    dictcache[user] = (result, now)#cache the result by user
			else:
				print('cache hits')
		else:
			result = func(user)
			dictcache[user] = (result, now)
		return result
	return __decorator

def login(user):
	print('in login:' + user)
	msg = validate(user)
	return msg

@cache#apply the cache for this slow validation
def validate(user):
    time.sleep(5)#simulate 10 second block
    msg = "success" if user == "jatsz" else "fail"
    return msg

result1 = login('jatsz'); print result1
result2 = login('jatsz'); print result2#this login will return immediately by hit the cache
result3 = login('candy'); print result3

"""
不改变被包装的函数，就能在它之上添加更多功能。

装饰器函数需要实现__decorator方法；


"""