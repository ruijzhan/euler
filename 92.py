#!/usr/bin/env python

def get_next(n):
    return sum([int(x)**2 for x in str(n)])

results = {}

def get_end_number(n):
    lis = [n]
    n_current = n
    while True:
        n_next = get_next(n_current)
        if n_next in results.keys():
            for i in lis:
                results[i]=n_next
            return results[n_next]

        if n_next in lis:
            for i in lis:
                results[i]=n_next
            return n_next

        n_current = n_next
        lis.append(n_next)

n=0
for i in xrange(1,10000000):
    if get_end_number(i) == 89:
        n+=1
        print n,i

print n

