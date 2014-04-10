#!/usr/bin/env python
import math

def remove_0_keep_5(n):
    while n%10 ==0:
        n/=10

    return int(str(n)[-5:])

def remove_0(n):
    while n%10 ==0:
        n/=10
    return n

res =1
for i in xrange(1,1000000000001):
    print i
    i = remove_0(i)
    res *=i
    res = remove_0_keep_5(res)

print res
