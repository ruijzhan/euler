#Even Fibonacci numbers
#Problem 2
#
#Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:
#
#    1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
#
#    By considering the terms in the Fibonacci sequence whose values do not exceed four million (4 000 000), find the sum of the even-valued terms.

def append_fib_seq(seq):
    seq.append(seq[-1]+seq[-2])
    return seq

fib_seq = [1,2]

while fib_seq[-1]<4000000:
    fib_seq = append_fib_seq(fib_seq)

n =0
for i in fib_seq:
    if i%2==0:
        n=n+i

print n
