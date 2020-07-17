import math


def summation(num):
    return 1 if num == 1 else summation(num-1) + num

def guess(k):
    return round(math.sqrt(k*2))

n = int(input())
g = guess(n)
if n == summation(g):
    print(g)
else:
    print(g-1)
