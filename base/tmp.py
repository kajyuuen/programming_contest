# https://qiita.com/_-_-_-_-_/items/34f933adc7be875e61d0
# abcde	s=input()	s='abcde'
# abcde	s=list(input())	s=['a', 'b', 'c', 'd', 'e']
# 5(1つだけ)	a=int(input())	a=5
# 1 2	| x,y = map(int,input().split())   |	x=1,y=2
# 1 2 3 4 5 ... n 　	li = input().split()	li=['1','2','3',...,'n']
# 1 2 3 4 5 ... n 　	li = inpl()	li=[1,2,3,4,5,...,n]
# FFFTFTTFF 　	li = input().split('T')	li=['FFF', 'F', '', 'FF']

# INPUT
# 3
# hoge
# foo
# bar
# ANSWER
# n=int(input())
# string_list=[input() for i in range(n)]

import math
import copy
from collections import defaultdict, Counter
from itertools import product
from bisect import bisect_left, bisect_right
# import numpy as np

def s_inpl(): return map(int,input().split())
def inpl(): return list(map(int, input().split()))
INF = float("inf")