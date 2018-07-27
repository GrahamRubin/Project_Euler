from math import sqrt
from pupy.maths import pytriple_gen

def tri_area(two_sides_len, other_side_length):
    return ( sqrt(two_sides_len**2 - (other_side_length/2.0)**2) *(other_side_length/2.0) ) % 1 == 0

print sum(sum(triple) for triple in  [(tri[0]*2, tri[2], tri[2]) for tri in [x for x in pytriple_gen((3+10**9)//3) if abs(x[2]-2*x[0]) == 1]])

# sum = 0
# for i in range(2, 1000000000//3):
#     if tri_area(i, i+1):
#         sum += 3*i+1
#     if tri_area(i, i-1):
#         sum += 3*i -1
#
# print sum

