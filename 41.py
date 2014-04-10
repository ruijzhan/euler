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

def ispandigital(n):
    for c in str(n):
        if str(n).count(c) >1:
            return False
    return True

for i in xrange(2,10000000000):
    if ispandigital(i):
        if isprime(i):
            print i
