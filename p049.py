from itertools import permutations
from itertools import combinations

def factors(n):
    return set(reduce(list.__add__, ([i, n//i] for i in range(1, int(pow(n, 0.5) + 1)) if n % i == 0)))


def prime_perms(n):
    return set(number for number in (int(''.join(x)) for x in set(permutations(i for i in str(n))) if "0" not in x) if len(factors(number)) == 2)


def check_set_for_answer(set_buddy):
    combos = [sorted(x) for x in combinations(set_buddy, 3)]
    for triplet in combos:
        if triplet[1]-triplet[0] == triplet[2]-triplet[1]:
            return [str(x) for x in triplet]
    return None


list_of_sets = []
for i in range(1000,10000):
    if len(factors(i)) == 2:
        permutes = prime_perms(i)
        if len(permutes) >= 3:
            group = check_set_for_answer(permutes)
            if group != None:
                print ''.join(group)
















