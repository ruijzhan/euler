#!/usr/bin/env python

n=13082761331670030 
res = 0
for i in xrange(2,n):
    if i**3 % n == 1:
        res += i

print res
