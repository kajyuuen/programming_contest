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
# URL: http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=DPL_1_A&lang=ja
######

def solve(a, b):
    len_a, len_b = len(a), len(b)

    dp = [ [0] * (len_b+1) for _ in range(len_a+1)]

    for i in range(1, len_a+1):
        for j in range(1, len_b+1):
            if a[i-1] == b[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i][j-1], dp[i-1][j])
    return dp[len_a][len_b]

def main():
    n = i_inpl()
    anss = []
    for _ in range(n):
        a = input()
        b = input()
        anss.append(solve(a, b))
    
    for ans in anss:
        print(ans)

if __name__ == "__main__":
    main()