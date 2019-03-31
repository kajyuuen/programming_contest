# メモ化再帰
# FIXME: なんか動かない
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

# 最小化問題なのでINFに初期化
INF = float("inf")
dp = [ INF ] * N

def solve(i):
    # DPの値が更新されていたらそのまま
    if dp[i] < INF:
        return dp[i]

    # 足場0のコストは0
    if i == 0:
        return 0

    # dp[i]の計算
    res = INF
    ## 足場i-1から来た場合
    res = min(res, solve(i-1) + abs(h[i] - h[i-1]))
    ## 足場i-2から来た場合
    if i > 1:
        res = min(res, solve(i-2) + abs(h[i] - h[i-2]))

    # メモ
    dp[i] = res

    return res


print(solve(N-1))