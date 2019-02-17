# a, bの最大公約数
def gcd(a,b):
    if b == 0:
        return a
    else:
        return gcd(b,a%b)

# リストnumbers最大公約数
def gcdlist(numbers):
    a = numbers[0]
    for i in range(len(numbers)):
        a = gcd(a, numbers[i])
    return a

if __name__ == "__main__":
    print(gcdlist([2, 10, 8, 40]))
    print(gcdlist([5, 13, 8, 1000000000]))
    print(gcdlist([1000000000, 1000000000, 1000000000]))
