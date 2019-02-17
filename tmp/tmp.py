# https://qiita.com/_-_-_-_-_/items/34f933adc7be875e61d0
# abcde	s=input()	s='abcde'
# abcde	s=list(input())	s=['a', 'b', 'c', 'd', 'e']
# 5(1つだけ)	a=int(input())	a=5
# 1 2	| x,y = map(int,input().split())   |	x=1,y=2
# 1 2 3 4 5 ... n 　	li = input().split()	li=['1','2','3',...,'n']
# 1 2 3 4 5 ... n 　	li = list(map(int,input().split()))	li=[1,2,3,4,5,...,n]
# FFFTFTTFF 　	li = input().split('T')	li=['FFF', 'F', '', 'FF']

# INPUT
# 3
# hoge
# foo
# bar
# ANSWER
# n=int(input())
# string_list=[input() for i in range(n)]

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
