def get_next(n):
    if n == 1 or n == 0:
        return 1
    if n%2 == 0:
        return n/2
    else:
        return n*3+1

len_dict = {}

def get_seq_len(n):
    length = 1
    lst = []
    n_found = False
    while n>=1 and not n in len_dict:
        lst.append(n)
        if n==1:
            break
        n = get_next(n)
        if not n in len_dict:
            length +=1

    if n in len_dict:
        length += len_dict[n]
        n_found = True

    for i in lst:
        len_dict[i]=len(lst)-lst.index(i)
        if n_found:
            len_dict[i] += len_dict[n]
    return length

i=1
while i<1000000:
    get_seq_len(i)
    i+=1

for key in len_dict.keys():
    print len_dict[key],key
