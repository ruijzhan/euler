#!/usr/bin/env python

numbers = list()

def fifth_power_sum(num):
    return sum([int(x)**5 for x in str(num)])

def fifth_power_sum_equal(num):
    if num == fifth_power_sum(num):
        return True
    else:
        return False

num = 2
while True:
    if fifth_power_sum_equal(num):
        numbers.append(num)
        print sum(numbers)
    num+=1
