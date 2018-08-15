from pupy.maths import *


def brute_force_pytriples(max_hype):
    for a in range(4, int(sqrt((max_hype**2)//2)+1)):
        for b in range(2, a):
            c = sqrt(a**2 + b**2)
            if c <= max_hype and int(c) == c:
                yield (b, a, int(c))
            elif c > max_hype:
                break

py_trips = sorted([x for x in brute_force_pytriples(1500000//2)])

sum_counts = {}
for trip in py_trips:
    summation = sum(trip)
    try:
        sum_counts[summation] += 1
    except KeyError:
        sum_counts.update({summation: 1})
    # if summation in sum_counts:
    #     sum_counts[summation] += 1
    # else:
    #     sum_counts[summation] = 1
count = 0
for entry in sum_counts:
    if sum_counts[entry] == 1:
        count += 1
print count
print max(sum_counts)





