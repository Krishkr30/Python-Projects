def sieve_of_eratosthenes(n: int) -> list[int]:
    is_prime = [True] * (n + 1)
    p = 2
    while p * p <= n:
        if is_prime[p]:
            for i in range(p * p, n + 1, p):
                is_prime[i] = False
        p += 1
    return [num for num in range(2, n + 1) if is_prime[num]]

if __name__ == "__main__":
    limit = 50
    print(f"Prime numbers up to {limit}: {sieve_of_eratosthenes(limit)}")
