def sieve_of_eratosthenes(N):
    prime_table = [True] * N
    prime_table[0] = prime_table[1] = False

    for i, is_prime in enumerate(prime_table):
        if is_prime:
            for n in range(i*i, N, i):
                prime_table[n] = False
    return prime_table

if __name__ == "__main__":
    print(sieve_of_eratosthenes(3))
    print(sieve_of_eratosthenes(11))