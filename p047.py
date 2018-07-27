

def factors(n):
    return set(reduce(list.__add__, ([i, n//i] for i in range(1, int(pow(n, 0.5) + 1)) if n % i == 0)))


def has_four_distinct_factors(n):
    if (len(set(x for x in factors(n) if x != n and len(factors(x))==2)) == 4):
        return n
    else:
        return 0

consecutive_nums = set()
i = 646
while len(consecutive_nums) != 4:
    consecutive_nums.clear()
    for a in range(0,4):
        if (has_four_distinct_factors(i+a) == a+i):
            consecutive_nums.add(a+i)
    i += 1
print consecutive_nums[0]