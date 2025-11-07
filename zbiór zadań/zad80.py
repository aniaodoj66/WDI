# dobrze

import math

def is_prime(x):
    if x == 0 or x == 1:
        return False
    if x == 2 or x == 3:
        return True
    for i in range(2, math.isqrt(x) + 1):
        if x % i == 0:
            return False
    return True

def pop(t1, t2):

    n = len(t1)
    max_mask = 3 ** n
    prime_sums = 0
    for mask in range(max_mask):
        current_sum = 0
        temp = mask
        for i in range(n):
            r = temp % 3
            temp = temp // 3
            if r == 0:
                current_sum += t1[i]
            elif r == 1:
                current_sum += t2[i]
            else:
                current_sum += t1[i] + t2[i]
        if is_prime(current_sum):
            prime_sums += 1
    return prime_sums


n1 = [2, 3, 5]
n2 = [7, 11, 13]

print(pop(n1,n2))