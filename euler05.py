"""
Smallest Multiple

2520 is the smallest number that can be divided by each
of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly
divisible by all of the numbers from 1 to 20.
"""

from math import sqrt

def is_prime(n): 
    for a in range(2, int(sqrt(n))): 
        if n % a == 0: 
            return False 
    return True 


def largest_prime_factor(n):
    i = 2
    a = n
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
    return [n, max([i for i in range(a) if n ** i <= a])]


def euler05(upper) -> int:
    total = 1
    pairs = []
    for i in range(1, upper + 1):
        current_pair = largest_prime_factor(i)
        print("current_pair ->", current_pair)
        done_with_pair = False
        for pair in pairs:
            if pair[0] == current_pair[0] and pair[1] >= current_pair[1]:
                done_with_pair = True
                break
            if pair[0] == current_pair[0] and pair[1] < current_pair[1]:
                pairs.remove(pair)
                pairs.append(current_pair)
                done_with_pair = True
                break
        if not done_with_pair:
            pairs.append(current_pair)
    for pair in pairs: total *= pair[0] ** pair[1]
    print("pairs ->", pairs)
    return total


print(euler05(10))
