#-*- encoding:utf-8 -*-

"""
For large amounts of data, it may be more efficient to use an array instead of a list. 
Since the array is limited to a single data type, it can use a more compact memory 
representation than a general purpose list. As an added benefit, arrays can be 
manipulated using many of the same methods as a list, so it may be possible to 
replaces lists with arrays in to your application without a lot of other changes.
"""

import array
"""
跟list的用法一样一样的
"""


import binascii

s = 'This is the array.'
a = array.array('c', s)

print 'As string:', s
print 'As array :', a
print 'As hex   :', binascii.hexlify(a)






"""
>>> dir(array)
['__add__', '__class__', '__contains__', '__copy__', '__deepcopy__', 
'__delattr__', '__delitem__', '__delslice__', '__doc__', '__eq__', 
'format__', '__ge__', '__getattribute__', '__getitem__', '__getslice__', 
'__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__iter__', 
'__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', 
'__reduce__', '__reduce_ex__', '__repr__', '__rmul__', '__setattr__', 
'__item__', '__setslice__', '__sizeof__', '__str__', '__subclasshook__', 
'append', 'buffer_info', 'byteswap', 'count', 'extend', 'fromfile', 
'fromlist', 'fromstring', 'fromunicode', 'index', 'insert', 'itemsize', 
'pop', 'read', 'remove', 'reverse', 'tofile', 'tolist', 'tostring', 
'tounicode', 'typecode', 'write']

>>> a1 = array('i',[1,2,3,4,5])
>>> print a1
array('i', [1, 2, 3, 4, 5])
>>> a1[2]
3
>>> print a1[2:3]
array('i', [3])
>>> print a1[2:4]
array('i', [3, 4])
>>> for i in a1:
...     print i
...
1
2
3
4
5
>>> a1.append(6)
>>> print a1
array('i', [1, 2, 3, 4, 5, 6])
>>> a1.extend(array('i',[7,8,9]))
>>> print a1
array('i', [1, 2, 3, 4, 5, 6, 7, 8, 9])
>>> a1.pop(3)
4
>>> a1.pop()
9
>>> a1.byteswap()
>>> parint a1.byteswap()
  File "<stdin>", line 1
    parint a1.byteswap()
            ^
SyntaxError: invalid syntax
>>> print a1.byteswap()
None
>>> a1
array('i', [1, 2, 3, 5, 6, 7, 8])
>>> a1.itemsize
4
>>> print [i for i in a1]
[1, 2, 3, 5, 6, 7, 8]
>>> a1.extend([1,2,3,])
>>> print a1
array('i', [1, 2, 3, 5, 6, 7, 8, 1, 2, 3])
>>> a1.sort()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'array.array' object has no attribute 'sort'
>>>
"""
