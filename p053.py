import math


def nCr(n,r):
    return math.factorial(n)/(math.factorial(r)*math.factorial(n-r))

lst = []

for n in range (23,101):
    for r in range(1,n):
        combo = nCr(n, r)
        if combo > 1000000:
            lst.append(combo)
print(len(lst))


