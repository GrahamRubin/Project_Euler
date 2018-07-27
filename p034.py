import math


def all_digits(n):
    digits = 0
    while n > 0:
        digits += (math.factorial(n%10))
        n //= 10
    return digits



sum = 0
for i in range(3,10000001):
    if i == all_digits(i):
        sum += i
print sum