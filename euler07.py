"""
By listing the first six prime numbers:
        2, 3, 5, 7, 11 and 13,
we can see that the 6th prime number is 13.
What is the 10.001st prime number?
"""

from math import log

# import time

# start_time = time.time()

def eratosthenes_nth(limit, n):
    sieve = [True] * (limit + 1)
    count = 0
    for num in range(2, limit + 1):
        if sieve[num]:
            count += 1
            if count == n:
                return num
            for i in range(num * num, limit + 1, num):
                sieve[i] = False

def euler07(n) -> int:
    return eratosthenes_nth(int(n * (log(n) + log(log(n)))), n)

# end_time = time.time()
# print(f"Elapsed time: {end_time - start_time} seconds")

print(euler07(10001))
