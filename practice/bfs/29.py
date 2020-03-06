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

field = None
number_of_moves = None
R, C = None, None
def bfs(sy, sx):
    global field, number_of_moves, R, C
    q = deque([[sy, sx]])
    number_of_moves[sy][sx] = 0
    
    while q:
        y, x = q.popleft()
        currenct_d = number_of_moves[y][x]
        for i in range(4):
            ny, nx = y+dy[i], x+dx[i]
            if inside(ny, nx, R, C) and field[ny][nx] == ".":
                if number_of_moves[ny][nx] == -1:
                    number_of_moves[ny][nx] = currenct_d + 1
                    q.append([ny, nx])


def main():
    global field, number_of_moves, R, C

    R, C = l_inpl()
    sy, sx = l_inpl()
    gy, gx = l_inpl()
    sy, sx, gy, gx = sy-1, sx-1, gy-1, gx-1
    field = [input() for _ in range(R)]
    number_of_moves = [ [-1]*C for _ in range(R)]

    bfs(sy, sx)
    print(number_of_moves[gy][gx])

if __name__ == "__main__":
    main()