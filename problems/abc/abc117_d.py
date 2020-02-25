# abcde    s=input()    s='abcde'
# abcde    s=list(input())    s=['a', 'b', 'c', 'd', 'e']
# 5(1つだけ)    a=int(input())    a=5
# 1 2    | x,y = s_inpl()   |    x=1,y=2
# 1 2 3 4 5 ... n 　    li = input().split()    li=['1','2','3',...,'n']
# 1 2 3 4 5 ... n 　    li = inpl()    li=[1,2,3,4,5,...,n]
# FFFTFTTFF 　    li = input().split('T')    li=['FFF', 'F', '', 'FF']

# INPUT
# 3
# hoge
# foo
# bar
# ANSWER
# n=int(input())
# string_list=[input() for i in range(n)]

import math
import copy
from collections import defaultdict
from collections import Counter
from collections import deque
# 直積 A={a, b, c}, B={d, e}:のとき，A×B={(a,d),(a,e),(b,d),(b,e),(c,d),(c,e)}: product(A, B)
from itertools import product
# 階乗 P!: permutations(seq), 順列 {}_len(seq) P_n: permutations(seq, n)
from itertools import permutations
# 組み合わせ {}_len(seq) C_n: combinations(seq, n)
from itertools import combinations
from bisect import bisect_left, bisect_right
# import numpy as np

def inside(y, x, H, W):
    return 0 <= y < H and 0 <= x < W

# 四方向: 右, 下, 左, 上
dy = [0, -1, 0, 1]
dx = [1, 0, -1, 0]

def i_inpl(): return int(input())
def s_inpl(): return map(int,input().split())
def l_inpl(): return list(map(int, input().split()))
INF = float("inf")
MAX_DIGIT = 50

############
############
############

N, K = l_inpl()
A = l_inpl()

# dp[上からi桁まで][smaller]
# smaller=0: X=K
# smaller=1: X<K
dp = [[-1] * 2 for _ in range(MAX_DIGIT+1)]
dp[0][0] = 0

for d in range(1, MAX_DIGIT+1):
    mask = 1<<(MAX_DIGIT - d)

    # A[i]においてd桁目にビットが立っているものの個数
    cnt = 0
    for i in range(N):
        if A[i] & mask:
            cnt += 1

    # Xのd桁目を0, 1にしたときのコスト
    cost0 = mask * cnt
    cost1 = mask * (N - cnt)

    # Kのd桁目が1だったとき
    if mask & K:
        # X=K -> X=K
        dp[d][0] = dp[d-1][0] + cost1
        if dp[d-1][1] == -1:
            # d = 1のとき
            dp[d][1] = cost0
        else:
            # X=K, X<K -> X<K
            dp[d][1] = max(dp[d-1][0] + cost0, dp[d-1][1] + max(cost0, cost1))
    # Kのd桁目が0だったとき
    else:
        # X=K -> X=K
        dp[d][0] = dp[d-1][0] + cost0
        # X<K -> X<K
        # X=K -> X<Kはd桁目が0のためありえない
        if dp[d-1][1] != -1:
            dp[d][1] = max(dp[d-1][1] + cost0, dp[d-1][1] + cost1)
    

print(max(dp[MAX_DIGIT][0], dp[MAX_DIGIT][1]))

