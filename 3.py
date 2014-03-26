#Largest prime factor
#Problem 3
#
#The prime factors of 13195 are 5, 7, 13 and 29.
#
#What is the largest prime factor of the number 600851475143 ?

def isprime(n):
    '''check if integer n is a prime'''
# make sure n is a positive integer
    n = abs(int(n))
# 0 and 1 are not primes
    if n < 2:
        return False
# 2 is the only even prime number
    if n == 2:
        return True
# all other even numbers are not primes
    if not n & 1:
        return False
# range starts with 3 and only needs to go up the squareroot of n
# for all odd numbers
    for x in range(3, int(n**0.5)+1, 2):
        if n % x == 0:
            return False
    return True


n = 600851475143
answer = 0
i=1
while i<n:
    i+=1
    if not isprime(i):
        continue
    else:
        if n%i != 0:
            continue
        else:
            n=n/i
            answer=i


print answer
