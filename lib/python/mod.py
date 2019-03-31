MOD = 1000000007

MOD = 1000000007

# 割り算
def power(a, b):
    if b == 0:
        return 1
    elif b % 2 == 0:
        d = power(a, b/2)
        return (d * d) % MOD
    elif b % 2 == 1:
        return (a * power(a, b-1)) % MOD

def div(a, b):
    return (a * power(b, MOD-2)) % MOD

if __name__ == "__main__":
    print(3000000000, 2)
