#!/usr/bin/env python

def isprime(n):
    '''check if integer n is a prime'''
    n = abs(int(n))
    if n < 2:
        return False
    if n == 2:
        return True
    if not n & 1:
        return False
    for x in range(3, int(n**0.5)+1, 2):
        if n % x == 0:
            return False
    return True

n = 2
s = 0
ps = 0
old_ps = 0
while True:
    if isprime(n):
        print n,
        s +=n
        old_ps = ps
        if isprime(s):
            ps = s
        if ps > 1000:
            print
            break
    n +=1

print old_ps
