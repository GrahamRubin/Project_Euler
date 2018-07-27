import math
import operator


def factors(n):
    return set(reduce(list.__add__, ([i, n//i] for i in range(1, int(pow(n, 0.5) + 1)) if n % i == 0)))


def rad(n):
    return reduce(operator.mul, set(x for x in factors(n) if len(factors(x)) == 2), 1)
randicands = []
for i in range(1, 100001):
    randicands.append((rad(i), i))

randicands.sort()

print(randicands[9999][1])

