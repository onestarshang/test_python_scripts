#coding:utf-8

"""
http://stackoverflow.com/questions/1059559/python-strings-split-with-multiple-separators/19211729#19211729
"""

from itertools import groupby
sep = ' ,-!?'
s = "Hey, you - what are you doing here!?"
print [''.join(g) for k, g in groupby(s, sep.__contains__) if not k]



"""
sep.__contains__ is a method used by 'in' operator. Basically it is the same as

lambda ch: ch in sep
but is more convenient here.

groupby gets our string and function. It splits string in groups using that function: 
whenever a value of function changes - a new group is generated. So, sep.__contains__ is 
exactly what we need.

groupby returns a sequence of pairs, where pair[0] is a result of our function and pair[1] 
is a group. Using 'if not k' we filter out groups with separators 
(because a result of sep.__contains__ is True on separators). 
Well, that's all - now we have a sequence of groups where each one 
is a word (group is actually an iterable so we use join to convert it to string).

This solution is quite general, because it uses a function to separate string 
(you can split by any condition you need). Also, it doesn't create intermediate strings/lists 
(you can remove join and the expression will become lazy, since each group is an iterator)

"""