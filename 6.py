def sum_square(lis):
    res = []
    for i in lis:
        res.append(i**2)
    return sum(res)

def square_sum(lis):
    return sum(lis)**2

print square_sum(range(1,101)) - sum_square(range(1,101))
