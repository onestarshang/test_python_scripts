#coding:utf-8

"""
最大公约数
gcd(m, n) = gcd(n, m mod n)
这个定理的意思是：整数m、n的最大公约数等于n和m除以n的余数的最大公约数。

最小公倍数等于两数之积除以最大公约数
"""

# calculate the greatest common divisor
def gcd(first, second):
	if (first < second):
		first, second = second, first
	while second != 0:
		first, second = second, first % second
	return first

# calculate the least common multiple
def lcm(first, second):
	gcd_num = gcd(first, second)
	return first * second / gcd_num
