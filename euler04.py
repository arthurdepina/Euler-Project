"""
Largest Palindrome Product

A palindromic number reads the same both ways. The largest palindrome
made from the product of two 2-digit numbers is 9009 = 91 * 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""

def isPalindrome(n) -> bool:
    return str(n) == str(n)[::-1]

def euler04() -> int:
    palindrome = 0
    for i in range (100, 1000):
        for j in range(100, 1000):
            if isPalindrome(i * j) and i * j > palindrome: palindrome = i * j
    return palindrome

print(euler04())


# from itertools import product

# def is_palindrome(num):
#     return str(num) == str(num)[::-1]

# multiples = ( (a, b) for a, b in product(xrange(100,999), repeat=2) if is_palindrome(a*b) )
# print max(multiples, key=lambda (a,b): a*b)

# https://stackoverflow.com/questions/12674389/highest-palindrome-with-3-digit-numbers-in-python
