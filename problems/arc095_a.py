import collections
import math
import numpy as np

#### START
n = int(input())
li = list(map(int,input().split()))
s_li = sorted(li)
left_num = s_li[n//2-1]
right_num = s_li[n//2]
for i in li:
    if i>left_num:
        print(left_num)
    else:
        print(right_num)