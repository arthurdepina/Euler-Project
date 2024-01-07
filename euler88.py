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

from functools import reduce

p_s = 9223372036854775807
stop = False
count = 0
maior = False

def product_sum(k, current_array=[]):
    global p_s
    if len(current_array) == k:
        # print(current_array)
        sum_array = sum(current_array)
        if (sum_array == reduce((lambda x, y: x * y), current_array)) and sum_array < p_s:
            p_s = sum_array
            return
        return
    for i in range(1, k + 1):
        product_sum(k, current_array + [i])

# product_sum(6)
# print(p_s)

def euler88(upper) -> int:
    global p_s
    global stop
    product_sums = []
    for i in range(2, upper + 1):#
        # print(i, end=" ")
        product_sum(i)
        # print(p_s)
        if p_s not in product_sums: product_sums.append(p_s)
        p_s = 9223372036854775807
        stop = False
    return sum(product_sums)


print(euler88(6))  # 30
# print(euler88(12)) # 61
# print(euler88(12000))
