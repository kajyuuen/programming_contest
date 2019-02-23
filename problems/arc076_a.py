from collections import defaultdict, Counter
import math
from bisect import bisect_left, bisect_right
import numpy as np

mod = 1000000007

def mul(a, b):
    return ((a % mod) * (b % mod)) % mod

#### START
n, m = map(int,input().split())

if n==m:
    a = math.factorial(n)
    print(mul(mul(a, a), 2))
elif n==m-1 or n-1==m:
    if n<m:
        a = math.factorial(n)
        b = a*m
    else:
        a = math.factorial(m)
        b = a*n
    print(mul(a, b))
else:
    print(0)