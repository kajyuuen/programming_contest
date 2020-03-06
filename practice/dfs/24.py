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
# URL: http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_4_B&lang=ja
######

i = 1
is_visited = None
d, f = {}, {}
def dfs(G, node):
    global i, is_visited, d, f
    if is_visited[node]:
        return

    is_visited[node] = True
    d[node] = i

    i += 1

    for next_node in G[node]:
        dfs(G, next_node)
    f[node] = i
    i += 1

def main():
    n = i_inpl()
    G = {} # Dict[list[]]
    for _ in range(n):
        l = l_inpl()
        G[l[0]] = l[2:]

    global i, is_visited, d, f
    is_visited = [False for _ in range(n+1)]

    dfs(G, 1)

    # 孤立しているノード
    for node in range(1, n+1):
        dfs(G, node)
    
    for i in range(1, n+1):
        print(i, d[i], f[i])

if __name__ == "__main__":
    main()