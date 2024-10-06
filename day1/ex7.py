import asyncio
import time

# 소수 판별 (O(N) 복잡도)
def is_prime_o_n(num):
    if num < 2:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

# 소수 판별 (O(√N) 복잡도)
def is_prime_o_sqrt_n(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

# 소수 판별 (에라토스테네스의 체, O(N log log N) 복잡도)
def sieve_of_eratosthenes(n):
    sieve = [True] * (n + 1)
    sieve[0], sieve[1] = False, False
    for i in range(2, int(n**0.5) + 1):
        if sieve[i]:
            for j in range(i*i, n + 1, i):
                sieve[j] = False
    return [num for num, is_prime in enumerate(sieve) if is_prime]

# 비동기 함수들
async def print_primes_o_n(n):
    start_time = time.time()
    primes = [num for num in range(n + 1) if is_prime_o_n(num)]
    print(f"\nPrimes with O(N) complexity - Time taken: {time.time() - start_time:.4f} seconds")
    return primes

async def print_primes_o_sqrt_n(n):
    start_time = time.time()
    primes = [num for num in range(n + 1) if is_prime_o_sqrt_n(num)]
    print(f"\nPrimes with O(√N) complexity - Time taken: {time.time() - start_time:.4f} seconds")
    return primes

async def print_primes_sieve(n):
    start_time = time.time()
    primes = sieve_of_eratosthenes(n)
    print(f"\nPrimes with O(N log log N) complexity (Sieve of Eratosthenes) - Time taken: {time.time() - start_time:.4f} seconds")
    return primes

# 메인 비동기 실행 함수
async def main():
    n = int(input("Enter a number (N): "))
    results = await asyncio.gather(
        print_primes_sieve(n),
        print_primes_o_sqrt_n(n),
        print_primes_o_n(n)
    )
    print("\nPrimes calculated:")
    print(results[0])

# 이벤트 루프 실행
asyncio.run(main())