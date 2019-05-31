from operator import mul
from functools import reduce

def per(n, r):
    if r == 0: 
        return 1
    return reduce(mul, range(n, n - r, -1))

if __name__ == "__main__":
    print(per(5, 2))
    print(per(4, 3))