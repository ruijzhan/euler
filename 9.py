a,b = 1,2
found = False

while not found:
    while True:
        c = 1000 -a -b
        if c<1:
            break
        if c**2 == a**2 + b**2 and a<b and b<c:
            found = True
            print a*b*c
        b+=1
    a+=1
    b=a+1

