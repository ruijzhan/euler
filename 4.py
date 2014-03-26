#coding=utf-8

def is_palindrome(num):
    num_str = str(num).encode('utf-8')
    for i in range(0,len(num_str)):
        if num_str[i] == num_str[-(i+1)]:
            continue
        else:
            return False
    return True

result = 0
for i in range(100,1000):
    for j in range(100,1000):
        if is_palindrome(i*j):
            if i*j > result:
                result = i*j
print result
    


