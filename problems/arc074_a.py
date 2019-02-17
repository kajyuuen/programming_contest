from collections import defaultdict, Counter
from math import pi, sqrt
from bisect import bisect_left, bisect_right

def req_S(h, w):
    tmp_s = []
    a_w = w
    for a_h in range(1, h):
        # b, cが横のパターン
        b_h = (h-a_h)//2
        c_h = h-b_h-a_h
        b_w, c_w = w, w
        S = [a_w*a_h, b_w*b_h, c_w*c_h]
        tmp_s.append(max(S)-min(S))
        # b, cが縦のパターン
        b_w = w//2
        c_w = w-b_w
        b_h, c_h = h-a_h, h-a_h
        S = [a_w*a_h, b_w*b_h, c_w*c_h]
        tmp_s.append(max(S)-min(S))
    return tmp_s

#### START
h, w = map(int,input().split())

all_S = req_S(h, w) + req_S(w, h)
print(min(all_S))
