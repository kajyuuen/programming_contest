import math
import copy
from collections import defaultdict, Counter
from itertools import product
from bisect import bisect_left, bisect_right
# import numpy as np

def s_inpl(): return map(int,input().split())
def inpl(): return list(map(int, input().split()))
INF = float("inf")

N = int(input())
act = []
for _ in range(N):
    act_i = inpl()
    act.append(act_i)

dp = [[0, 0, 0] for _ in range(N+1)]

for i in range(N):
    # 遷移先
    for j in range(3):
        # 遷移元
        for k in range(3):
            if j == k:
                continue
            dp[i+1][j] = max(dp[i+1][j], dp[i][k] + act[i][j])

ans = 0
for k in range(3):
    ans = max(ans, dp[N][k])

print(ans)