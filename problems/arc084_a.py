from collections import defaultdict, Counter
from math import pi, sqrt
from bisect import bisect_left, bisect_right

#### START
n = int(input())
a, b, c = list(map(int,input().split())), list(map(int,input().split())), list(map(int,input().split()))

a = sorted(a)
b = sorted(b)
c = sorted(c)

cnt = 0
for bi in b:
    alen = bisect_left(a, bi)
    clen = bisect_right(c, bi)
    if alen > 0 and clen < len(c):
        cnt += alen * (n - clen)

print(cnt)