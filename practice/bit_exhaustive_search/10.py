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
from bisect import bisect_left, bisect_right
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
# URL: http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_5_A&lang=ja
######

def main():
    N = i_inpl()
    A = [ int(i) for i in input().split(" ")]
    q = i_inpl()
    m = [ int(i) for i in input().split(" ")]

    # bit演算
    all_num = set()
    for i in range(1, 2**N):
        tmp = []
        for j in range(N):
            if ((i>>j) & 1):
                tmp.append(A[j])
        all_num.add(sum(tmp))

    for m_i in m:
        if m_i in all_num:
            print("yes")
        else:
            print("no")

if __name__ == "__main__":
    main()