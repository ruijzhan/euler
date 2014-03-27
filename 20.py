import math

num_str = str(math.factorial(100))

num_lis = []

for c in num_str:
    num_lis.append(int(c))

print sum(num_lis)
