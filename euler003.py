"""
Largest Prime Factor

The prime factors of 13195 are 5, 7, 14 and 29.

What is the largest prime factor of the number 
600851475143?
"""

from math import floor, sqrt

# import time
# start_time = time.time()

def eratosthenes(limit):
    primes = []
    sieve = [True] * (limit + 1)
    
    for num in range(2, limit + 1):
        if sieve[num]:
            primes.append(num)
            for i in range(num * num, limit + 1, num):
                sieve[i] = False
    
    return primes


def euler03(num):
    return next(i for i in eratosthenes(floor(sqrt(num)))[::-1] if num % i == 0)


print(euler03(600851475143))

# end_time = time.time()
# print(f"Elapsed time: {end_time - start_time} seconds")
