# -*- encoding:utf-8 -*-

class B(object):

 	def __call__(self, name):
 		return getattr(self, name)

 	def noattr(self, text):
 		print 'noattr' + text
 	
 	def b(self, text):
 		print 'b' + text


class A(object):

	def __getattr__(self, name):
		bb = B()
		return bb(name)

# a = A()
# a.noattr('\nno')
# a.b('bbbb')


class Prod:
 	def __init__(self, value):
 		self.value = value

 	def __call__(self, other):
 		return self.value * other


class foo(object):
    def f1(self):
        print("original f1")

    def f2(self):
        print("original f2")


class foo_decorator(object):
    def __init__(self, decoratee):
        self._decoratee = decoratee

    def f1(self):
        print("decorated f1")
        self._decoratee.f1()

    def seefunc(self):
    	return 'i can see this func'

    def __getattribute__(self, name):
    	print '*****************'
    	print name
    	print '*****************'
    	return object.__getattribute__(self, name)

    def __getattr__(self, name):
    	print '================='
    	print name
    	print '================='
        return getattr(self._decoratee, name)


u = foo()
v = foo_decorator(u)
v.seefunc()
v.f1()
v.f2()


"""
python 再访问属性的方法上定义了__getattr__() 和 __getattribute__() 2种方法，
其区别非常细微，但非常重要。

如果某个类定义了 __getattribute__() 方法，在 每次引用属性或方法名称时 Python 
都调用它（特殊方法名称除外，因为那样将会导致讨厌的无限循环）。
如果某个类定义了 __getattr__() 方法，Python 将只在正常的位置查询属性时才会调用它。
如果实例 x 定义了属性 color， x.color 将 不会 调用x.__getattr__('color')；而只会返回 x.color 已定义好的值。
 

让我们用两个例子来解释一下：



class Dynamo(object):
    def __getattr__(self, key):
        if key == 'color':         ①
            return 'PapayaWhip'
        else:
            raise AttributeError   ②

>>> dyn = Dynamo()
>>> dyn.color                      ③
'PapayaWhip'
>>> dyn.color = 'LemonChiffon'
>>> dyn.color                      ④
'LemonChiffon'



属性名称以字符串的形式传入 __getattr()__ 方法。如果名称为 'color'，该方法返回一个值。
（在此情况下，它只是一个硬编码的字符串，但可以正常地进行某些计算并返回结果。）
如果属性名称未知， __getattr()__ 方法必须引发一个 AttributeError 例外，否则在访问未定义属性时，
代码将只会默默地失败。（从技术角度而言，如果方法不引发例外或显式地返回一个值，它将返回 None ——Python 的空值。这意味着 所有 未显式定义的属性将为 None，几乎可以肯定这不是你想看到的。）
dyn 实例没有名为 color 的属性，因此在提供计算值时将调用 __getattr__() 。
在显式地设置 dyn.color 之后，将不再为提供 dyn.color 的值而调用 __getattr__() 方法，
因为 dyn.color 已在该实例中定义。
另一方面，__getattribute__() 方法是绝对的、无条件的。




class SuperDynamo(object):
    def __getattribute__(self, key):
        if key == 'color':
            return 'PapayaWhip'
        else:
            raise AttributeError

>>> dyn = SuperDynamo()
>>> dyn.color                      ①
'PapayaWhip'
>>> dyn.color = 'LemonChiffon'
>>> dyn.color                      ②
'PapayaWhip'




在获取 dyn.color 的值时将调用 __getattribute__() 方法。
即便已经显式地设置 dyn.color，在获取 dyn.color 的值时, 仍将调用 __getattribute__() 方法。
如果存在 __getattribute__() 方法，将在每次查找属性和方法时 无条件地调用 它，哪怕在创建
实例之后已经显式地设置了属性。
☞如果定义了类的 __getattribute__() 方法，你可能还想定义一个 __setattr__() 方法，
并在两者之间进行协同，以跟踪属性的值。否则，在创建实例之后所设置的值将会消失在黑洞中。

必须特别小心 __getattribute__() 方法，因为 Python 在查找类的方法名称时也将对其进行调用。




class Rastan(object):
    def __getattribute__(self, key):
        raise AttributeError           ①
    def swim(self):
        pass

>>> hero = Rastan()
>>> hero.swim()                        ②
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 3, in __getattribute__
AttributeError




该类定义了一个总是引发 AttributeError 例外的 __getattribute__() 方法。没有属性或方法的查询会成功。
调用 hero.swim() 时，Python 将在 Rastan 类中查找 swim() 方法。
该查找将执行整个 __getattribute__()方法，因为所有的属性和方法查找都通过__getattribute__() 方法。
在此例中， __getattribute__() 方法引发 AttributeError 例外，因此该方法查找过程将会失败，而方法调用也将失败。
"""