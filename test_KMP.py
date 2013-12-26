#coding:utf-8

import sys, os, time

def matchKMP(S, P):
    next = nextKMP(P)
    i = 0
    j = 0
    while i<len(S):
        if j==-1 or S[i] == P[j]:
            i +=1
            j +=1
        else:
            j = next[j]
        if j==len(P):
            return i-len(P)
    return -1

def nextKMP(P):
    n = [-1]
    
    k = -1
    q = 0
    while q < len(P) - 1:
        if k == -1 or P[q] == P[k]:
            k += 1
            q += 1
            n.append(k)
        else:
            k = n[k]
    return n


if __name__=='__main__':
    res = matchKMP('ababfdeababacersd','ababac')
    print res
    
