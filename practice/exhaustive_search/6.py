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
# URL: https://atcoder.jp/contests/sumitrust2019/tasks/sumitb2019_d
######

def main():
    N = i_inpl()
    base_S = input()
    ans = set()
    for i in range(1000):
        S = copy.deepcopy(base_S)
        find_num = str(i).zfill(3)
        k = S.find(find_num[0])
        if k == -1:
            continue

        S = S[k+1:]
        k = S.find(find_num[1])
        if k == -1:
            continue

        S = S[k+1:]
        k = S.find(find_num[2])
        if k == -1:
            continue

        ans.add(find_num)
    print(len(ans))

if __name__ == "__main__":
    main()