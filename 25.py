#!/usr/bin/env python

seq = (1,1)
term = 2

def fib_next_num(fib_seq):
    num = sum(fib_seq)
    return (fib_seq[1],num)

while True:
    seq = fib_next_num(seq)
    term+=1
    if len(str(seq[1])) >999:
        print term
        break
