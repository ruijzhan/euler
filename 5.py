def divisible(number,lst):
    for n in lst:
        if number%n != 0:
            return False
    return True



n=20
lis = range(2,21)
lis.reverse()
while True:
    print n
    if divisible(n,lis):
        break
    n+=20

print "Answer=%d"%(n)
