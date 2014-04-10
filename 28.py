#!/usr/bin/env python
import math

s = [(1+2*n)**2 for n in range(0,9-2)]

res = 0
for n in s:
    index = s.index(n)
    if index == 0:
        res +=1
    else:
        print [n,n-(math.sqrt(n)-1),n-(math.sqrt(n)-1)*2,n-(math.sqrt(n)-1)*3]
        res += sum([n,n-(math.sqrt(n)-1),n-(math.sqrt(n)-1)*2,n-(math.sqrt(n)-1)*3])

print res


