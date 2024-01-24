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
# 3*sqrt(2st) + 2s + 2t = 1000, and then:
# (s^2) * (4/9) + s [(-4000/9) - (10t/9)] + [(4t^2)/9] - [(4000t)/9] + [1000000/9]
#
# Solving with Bhaskara's:
# a = 4/9
# b = (-4000/9) - (10t/9) = (-4000/9) + [(-10/9)*t]
# c = [(4t^2)/9] - [(4000t)/9] + [1000000/9] = (4/9)*(t**2) + t(-4000/9) + 1000000/9

def solve_second_degree_equation(a, b, c):
    sols = list()
    d = (b**2) - (4*a*c)
    if d < 0: return None
    sol_a = (-b - sqrt(d))/(2*a)
    sol_b = (-b + sqrt(d))/(2*a)
    if sol_a == sol_b: return ([sol_a])
    if sol_a > 0: sols.append(sol_a)
    if sol_b > 0: sols.append(sol_b)
    return sols

def euler09(x) -> int:
    s_a = 4/9
    # b_1 = -4000/9
    # b_2 = -10/9
    # c_1 = 4/9
    # c_2 = -4000/9
    # c_3 = 1000000/9
    for t in range(1, 100):
        # s_b = (b_1 * t) + b_2
        # s_c = (c_1 * (t**2)) + (c_2 * t) + c_3
        possible_s = solve_second_degree_equation(4, (-10*t) - 4000, (4*(t**2)) - (4000*t) + 1000000)
        # print(possible_s)
        if not possible_s: continue
        for s in possible_s:
            r = sqrt(2*s*t)
            if not isinstance(r, int): continue
            if 3*r + 2*s + 2*t == 1000:
                return (r + s) * (r + t) * (r + s + t)


print(euler09(1000))
