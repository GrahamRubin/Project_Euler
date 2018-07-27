from functools import reduce
from itertools import combinations_with_replacement
from itertools import combinations
from pupy.maths import divisors_gen

# nums_with_sums = {1: [1], 2: [1]}
#
#
def factors(n):
    return set(reduce(list.__add__, ([i, n//i] for i in range(1, int(pow(n, 0.5) + 1)) if n % i == 0)))

def sum_divisors(n):
    return sum(divisor for divisor in factors(n) if divisor < n)


abundant_nums = set()
for i in range(1,28124):
    blah = sum_divisors(i)
    if blah > i:
        abundant_nums.add(i)
possible_sums = set(sum(pair) for pair in combinations_with_replacement(abundant_nums, 2))
print(sum(set(i for i in range(28124) if i not in possible_sums)))
