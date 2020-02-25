import math
import numpy as np
import copy
from collections import defaultdict, Counter
from itertools import product
from bisect import bisect_left, bisect_right
def inpl(): return list(map(int, input().split()))

li = list(map(int, input().split()))
N, A, B, C = li[0], li[1], li[2], li[3]
l = sorted([ int(input()) for i in range(N) ])

INF = 1e9

def dfs(ind, a, b, c):
    if ind == N:
        if min(a, b, c) > 0:
            return abs(a-A) + abs(b-B) + abs(c-C) - 30
        else:
            return INF
    ret0 = dfs(ind+1, a, b, c)
    ret1 = dfs(ind+1, a + l[ind], b, c) + 10
    ret2 = dfs(ind+1, a, b + l[ind], c) + 10
    ret3 = dfs(ind+1, a, b, c + l[ind]) + 10
    return min(ret0, ret1, ret2, ret3)

print(dfs(0, 0, 0, 0))