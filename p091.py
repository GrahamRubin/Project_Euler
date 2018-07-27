import math
from itertools import permutations, product

def is_right_triangle(P, Q):
    OP = math.sqrt(P[0]**2+P[1]**2)
    OQ = math.sqrt(Q[0]**2+Q[1]**2)
    PQ = math.sqrt((P[0]-Q[0])**2+(P[1]-Q[1])**2)
    if OP == 0 or OQ ==0 or PQ ==0:
        return False
    points = [OP, OQ, PQ]
    print points
    maximum = max(points)
    points.remove(maximum)
    return points[0]**2 + points[1]**2 == maximum**2


def all_tris_grid_n(n):
    count = 0
    possible_tris = [(tri[0:2], tri[2:4]) for tri in permutations(product(range(0,n+1), repeat=2), 4)]
    print possible_tris
    for tri in possible_tris:
        if is_right_triangle(tri[0], tri[1]):
            count += 1
    return count




print all_tris_grid_n(2)
