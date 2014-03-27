import math
def get_n_th_triangle_number(n):
    return sum(range(1,n+1))


def get_n_divisors(num):
    n_d = 0
    for i in range(1,int(num/2)+1):
        if num%i ==0:
            n_d +=1
    return n_d

    
i = 1
last_tri = 0
while True:
    tri = last_tri+i
    n_d = get_n_divisors(tri)
    print i,tri,n_d
    if n_d > 500:
        print "Answer:", tri
        break
    last_tri = tri
    i+=1
