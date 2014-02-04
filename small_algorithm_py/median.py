#coding:utf-8
##求一个list的中位数
def median(L):
    L.sort()
    m, l = divmod(len(L),2)
    print L[m] if l else (L[m]+L[m-1])/2 if (L[m]+L[m-1])%2==0 else "%.1f" % ((L[m]+L[m-1])/2.0)
