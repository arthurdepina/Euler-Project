"""
 The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
Find the sum of all the primes below two million.
"""

def eratosthenes(limit):
    primes = []
    sieve = [True] * (limit + 1)
    
    for num in range(2, limit + 1):
        if sieve[num]:
            primes.append(num)
            for i in range(num * num, limit + 1, num):
                sieve[i] = False
    
    return primes


def euler10(upper) -> int:
    return sum(eratosthenes(upper))


print(euler10(2000000))
