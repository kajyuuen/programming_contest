import math
import copy
from collections import defaultdict, Counter
from itertools import product
from bisect import bisect_left, bisect_right
# import numpy as np

def s_inpl(): return map(int,input().split())
def inpl(): return list(map(int, input().split()))
INF = float("inf")

N, W = s_inpl()
dp = [[0 for _ in range(W+1)] for _ in range(N+1)]

w, v = [], []
for _ in range(N):
    wi, vi = s_inpl()
    w.append(wi)
    v.append(vi)

for i in range(N):
    for sum_w in range(W+1):

        # i番目の品物が選べて，選ぶとき
        if sum_w >= w[i]:
            dp[i+1][sum_w] = max(dp[i+1][sum_w], dp[i][sum_w-w[i]] + v[i])

        # i番目の品物を選ばないとき
        dp[i+1][sum_w] = max(dp[i+1][sum_w], dp[i][sum_w])

print(dp[N][W])