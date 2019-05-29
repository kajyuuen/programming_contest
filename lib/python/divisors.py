def divisors(n):
    results = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            results.append(i)
            if i**2 == n:
                continue
            results.append(n//i)
    return results
