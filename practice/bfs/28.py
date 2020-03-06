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
# URL: http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_11_C&lang=ja
######

i = 0
is_visited = None
d = {}
def bfs(G, node):
    global i, is_visited, d
    q = deque([node])
    is_visited[node] = True
    d[node] = i
    
    while q:
        next_node = q.popleft()
        currenct_d = d[next_node]
        for node_neighbour in G[next_node]:
            if not is_visited[node_neighbour]:
                is_visited[node_neighbour] = True
                d[node_neighbour] = currenct_d + 1
                q.append(node_neighbour)

def main():
    n = i_inpl()
    G = {}
    for _ in range(n):
        l = l_inpl()
        G[l[0]] = l[2:]

    global is_visited
    is_visited = [False for _ in range(n+1)]

    bfs(G, 1)
    
    for i in range(1, n+1):
        di = d.get(i, -1)
        print(i, di)

if __name__ == "__main__":
    main()