import math
import sys
sys.setrecursionlimit(100000)

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

# 八方向
dxy = [[-1, 0], [-1, 1], [0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1]]

def i_inpl(): return int(input())
def l_inpl(): return list(map(int, input().split()))
INF = float("inf")

######
# URL: http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_4_B&lang=ja
######

field, w, h = None, None, None
def dfs(y, x):
    global field, w, h

    if not inside(y, x, h, w):
        return
    if field[y][x] == "0":
        return

    field[y][x] = "0"

    for i in range(8):
        ny, nx = y + dxy[i][0], x + dxy[i][1]
        dfs(ny, nx)


def main():
    global field, w, h

    anss = []
    while True:
        w, h = l_inpl()
        if w == 0 and h == 0:
            break
        field = [ input().split() for _ in range(h) ]
        ans = 0
        for hi in range(h):
            for wi in range(w):
                if field[hi][wi] == "1":
                    dfs(hi, wi)
                    ans += 1
        anss.append(ans)
    
    for ans in anss:
        print(ans)

if __name__ == "__main__":
    main()