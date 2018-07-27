from itertools import combinations

pent_nums = set((n*(3*n-1))//2 for n in range(1,10001))
d_values = set()
for pair in set(combinations(pent_nums, 2)):
    if sum(pair) in pent_nums and abs(pair[0]-pair[1]) in pent_nums:
        d_values.add(abs(pair[0]-pair[1]))

print(d_values)

