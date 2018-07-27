from itertools import combinations_with_replacement
import math

cache = {}

def num_int_solution(M):
    count = 0
    for cube in [x for x in combinations_with_replacement(range(1,M+1), 3)]:
        if min( math.sqrt((cube[0]+cube[1])**2+cube[2]**2), math.sqrt((cube[0]+cube[2])**2+cube[2]**2) ) % 1 == 0:
            count += 1
    return count


print num_int_solution(600)
n = 1000
solutions = num_int_solution(n)
while solutions < 1000000:
    n+=1
    solutions = num_int_solution(n)

print solutions
