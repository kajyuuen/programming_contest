import math
import copy
from operator import mul
from functools import reduce
from collections import defaultdict
from collections import Counter
from collections import deque
# 直積 A={a, b, c}, B={d, e}:のとき，A×B={(a,d),(a,e),(b,d),(b,e),(c,d),(c,e)}: product(A, B)
from itertools import product
# 階乗 P!: permutations(seq), 順列 {}_len(seq) P_n: permutations(seq, n)
from itertools import permutations
# 組み合わせ {}_len(seq) C_n: combinations(seq, n)
from itertools import combinations
from bisect import bisect_left #, bisect_right
# import numpy as np

def inside(y, x, H, W):
    return 0 <= y < H and 0 <= x < W

# 四方向: 右, 下, 左, 上
dy = [0, -1, 0, 1]
dx = [1, 0, -1, 0]

def i_inpl(): return int(input())
def l_inpl(): return list(map(int, input().split()))
INF = float("inf")

######
# URL: http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_10_A&lang=ja
######


def main():
    N, W = l_inpl()
    items = []
    for i in range(N):
        vi, wi = l_inpl()
        items.append([vi, wi])

    dp = [ [0] * (W+1) for _ in range(N+1) ]

    for i in range(N):
        for max_w in range(W+1):
            vi, wi = items[i]

            if max_w >= wi:
                dp[i+1][max_w] = max(dp[i+1][max_w], dp[i][max_w-wi] + vi)

            dp[i+1][max_w] = max(dp[i+1][max_w], dp[i][max_w])

    print(dp[N][W])

if __name__ == "__main__":
    main()