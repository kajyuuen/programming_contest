import math
import copy
from collections import defaultdict, Counter
# 直積 A={a, b, c}, B={d, e}:のとき，A×B={(a,d),(a,e),(b,d),(b,e),(c,d),(c,e)}: product(A, B)
from itertools import product
# 階乗 P!: permutations(seq), 順列 {}_len(seq) P_n: permutations(seq, n)
from itertools import permutations
# 組み合わせ {}_len(seq) C_n: combinations(seq, n)
from itertools import combinations
from bisect import bisect_left, bisect_right
# import numpy as np

def i_inpl(): return int(input())
def s_inpl(): return map(int,input().split())
def l_inpl(): return list(map(int, input().split()))
INF = float("inf")

N = i_inpl()
F = []
for _ in range(N):
    Fi = l_inpl()
    F.append(Fi)

P = []
for _ in range(N):
    Pi = l_inpl()
    P.append(Pi)


# bit全探索
ans = -1 * INF
# NOTE: 2**10(1024) != 2<<10(2048)
for i in range(1, 2**10):
    tmp = 0
    for j in range(N):
        c = 0
        # NOTE: iとF[j]のAND演算
        for k in range(10):
            if ((i>>k) & 1) & F[j][k]:
                c += 1
        tmp += P[j][c]
    ans = max(ans, tmp)

print(ans)