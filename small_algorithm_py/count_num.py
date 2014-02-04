#coding:utf-8

"""
给你一个正整数列表 L, 如 L=[2,8,3,50], 输出L内所有数字的乘积末尾0的个数,
如样例L的结果为2.(提示:不要直接相乘,数字很多,可能溢出)
"""

multi = 1
count = 0
for i in L:
    multi *= i
    while multi % 10 == 0:
        count += 1
        multi = multi / 10
    multi = multi % 10
print count


"""
给你一个正整数列表 L, 如 L=[2,8,3,50], 判断列表内所有数字乘积的最后一个非零数字的奇偶性,
奇数输出1,偶数输出0. 如样例输出应为0
"""

multi = 1
for i in L:
    multi *= i
    while multi % 10 == 0:
        multi = multi / 10
    multi = multi % 10
print multi % 2