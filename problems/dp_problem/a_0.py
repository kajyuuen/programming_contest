import math
import numpy as np
import copy
from collections import defaultdict, Counter
from itertools import product
from bisect import bisect_left, bisect_right

def s_inpl(): return map(int,input().split())
def inpl(): return list(map(int, input().split()))

N = int(input())
h = inpl()

INF = float('inf')

# 最小化問題なのでINFに初期化
dp = [ INF for _ in range(100010) ]

# 初期状態
dp[0] = 0

# ループ
for i in range(1, N):
    dp[i] = min(dp[i], dp[i-1] + abs(h[i] - h[i-1]))
    if i > 1:
        dp[i] = min(dp[i], dp[i-2] + abs(h[i] - h[i-2]))

print(dp[N-1])