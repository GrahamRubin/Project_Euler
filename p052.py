from itertools import combinations


def sort_and_join(n):
    return int(''.join(sorted([char for char in str(n)])))
#
# print sort_and_join(251748)
# print sort_and_join(125874)

def same_digits(list_of_multiples):
    for pair in combinations(list_of_multiples, 2):
        if sort_and_join(pair[0]) != sort_and_join(pair[1]):
            return False
    return True


for i in range(1,150000):
    if same_digits([i*x for x in range(1,7)]):
        print i