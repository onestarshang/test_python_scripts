#coding:utf-8
##求某个范围内的所有素数
def prime(n):
    lis = {}
    for i in xrange(2,n+1):     
        if not i in lis:
            lis[i] = 1
            k = i*2
            while k <= n:
                lis[k] = 0
                k = k+i
    ans = []    
    for i in lis:
        if lis[i] == 1:
            ans.append(i)
    return ans
