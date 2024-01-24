"""
Pythagorean triplet is a set of three natural numbers, a < b < c, for which
                            a^2 + b^2 = c^2
For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2
There exists exactly one Pythagorean triplet for which a + b + c = 1000/
Find the product abc.
"""
from math import sqrt

# we know from Dickson's method that to find integer solutions to
# a^2 + b^2 = c^2, we need to find positive integers r, s and t
# such that r^2 = 2*s*t. Then:
#
# a = r + s
# b = r + t
# c = r + s + t
#
# Since we want a + b + c = 1000
# r + s + t + r + t + r + s + t = 1000
# 3*r + 2*s + 2*t = 1000
# 3*sqrt(2*s*t) + 2*s + 2*t = 1000

def euler09(x) -> int:
    for s in range(1, 450):
        for t in range(1, 450):
            if 3*sqrt(2*s*t) + 2*s + 2*t == 1000:
                r = sqrt(2*s*t)
                a = r + s
                b = r + t
                c = r + s + t
                print(f"a = {a}, b = {b}, c = {c}")
                return a*b*c


print(euler09(1000))
