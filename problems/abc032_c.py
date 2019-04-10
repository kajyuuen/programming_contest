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

def s_inpl(): return map(int,input().split())
def inpl(): return list(map(int, input().split()))
INF = float("inf")

N, K = s_inpl()
s = [int(input()) for _ in range(N)]

if 0 in s:
    print(N)
else:
    l, r = 0, 0
    ans = 0
    p = 1
    while r < N:
        # 右端を進めたときの積がK以下なら右端を進める
        if p * s[r] <= K:
            p *= s[r]
            r += 1
            ans = max(ans, r - l)
        # 右端と左端が一致したとき，両端を進める
        elif r == l:
            r += 1
            l += 1
        # それ以外のとき左端を進める
        else:
            p //= s[l]
            l += 1

    print(ans)