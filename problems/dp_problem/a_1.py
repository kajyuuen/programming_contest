# 配るDP
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
dp = [ INF ] * N

# 初期状態
dp[0] = 0

# ループ
for i in range(0, N-2):
    dp[i+1] = min(dp[i+1], dp[i] + abs(h[i] - h[i+1]))
    dp[i+2] = min(dp[i+2], dp[i] + abs(h[i] - h[i+2]))

# 最後のノードについて確認
dp[-1] = min(dp[-1], dp[-2] + abs(h[-1] - h[-2]))
print(dp[N-1])