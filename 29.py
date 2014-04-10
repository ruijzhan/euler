#!/usr/bin/env python

terms = {}

for a in range(2,101):
    for b in range(2,101):
        terms[a**b] = None

print len(terms)
