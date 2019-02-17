# a, bの最大公約数
def gcd(a,b):
    if b == 0:
        return a
    else:
        return gcd(b,a%b)

# a, bの最小公倍数
def lcm(a, b):
    return a * b / gcd(a,b)

# リストnumbers最小公倍数
def lcmlist(numbers):
    a = numbers[0]
    for i in range(len(numbers)):
        a = lcm(a, numbers[i])
    return int(a)

if __name__ == "__main__":
    print(lcmlist([1, 2, 6]))
    print(lcmlist([3, 5]))
    print(lcmlist([24, 36]))
