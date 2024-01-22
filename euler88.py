"""
A natural number, N, that can be written as the sum and product of
a given set of at least two natural numbers, {a1, a2, ..., ak} is
called a product-sum number:
N = a1 + a2 + ... + ak = a1 * a2 * ... * ak

For example, 6 = 1 + 2 + 3 = 1 * 2 * 3

For a given set of size k, we shall call the smallest N with this
property a minimal product-sum number. The minimal product-sum
numbers for sets of size, k = 2, 3, 4, 5 and 6 are as follows:

k = 2: 4  =                 2 * 2 = 2 + 2
k = 3: 6  =             1 * 2 * 3 = 1 + 2 + 3
k = 4: 8  =         1 * 1 * 2 * 4 = 1 + 1 + 2 + 4
k = 5: 8  =     1 * 1 * 2 * 2 * 2 = 1 + 1 + 2 + 2 + 2
k = 6: 12 = 1 * 1 * 1 * 1 * 2 * 6 = 1 * 1 * 1 * 1 * 2 * 6

Hence for 2 <= k <= 6, the sum of all the minimal product-sum
numbers is 4 + 6 + 8 + 12 = 30; note that 8 is only counted once in
the sum.

In fact, as the complete set of minimal product-sum numbers for
2 <= k <= 12 is {4, 6, 8, 12, 15, 16}, the sum is 61.

What is the sum of all the minimal product-sum numbers for
2 <= k <= 12000?
"""
import time, math
from functools import cache
start_time = time.time()

def divisors(n):
    divisors = [n]
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            divisors.append(i)
            divisors.append(int(n/i))
    return sorted(set(divisors))

@cache
def poss_fact_length(n, new_n, product, a_sum, count):
    possibilities = []

    product = product
    a_sum = a_sum

    if product > n or a_sum > n:
        return []
    
    if product == n and a_sum == n:
        return [count]
    
    if n == 1:
        return [count + (n - a_sum)]
    
    divs = divisors(new_n)

    for div in divs:
        possibilities += poss_fact_length(n, new_n//div, product * div, a_sum + div, count + 1)

    return possibilities
    

def euler88(upper) -> int:
    minimal_product_sums = [float('inf')] * (2 * upper + 1)
    for num in range(4, 2*upper + 1):
        for k in set(poss_fact_length(num, num, 1, 0, 0)): # this set contains all lengths (k) for which num is the product-sum
            minimal_product_sums[k] = min(minimal_product_sums[k], num)
    minimal_product_sums = minimal_product_sums[2:upper + 1] # we only want m_p_s's from 2 <= k <= limit
    # so we're cutting index (k) 0, 1 and index's > limit.
    return sum(set(minimal_product_sums))

if __name__ == "__main__":
    print(euler88(12000))
    print("--- %s seconds ---" % (time.time() - start_time))

