
def det(u,v):
    return (u[0]*v[1]-u[1]*v[0])


def area(x1, y1, x2, y2, x3, y3):
    return abs((x1*(y2-y3) + x2*(y3-y1) + x3*(y1-y2))/2.0)


def is_inside(x1, y1, x2, y2, x3, y3, a, b):
    A = area(x1, y1, x2, y2, x3, y3)
    A1 = area(a, b, x2, y2, x3, y3)
    A2 = area(x1, y1, a, b, x3, y3)
    A3 = area(x1, y1, x2, y2, a, b)
    return A == A1 + A2 + A3


file = open("D:\\graham_temp\\peuler\\triangles.txt", "r")
triangle_strings = file.read().split('\n')
count = 0
for tri in triangle_strings:
    digits = tri.split(',')
    # num_lst = []
    # for sublst in lst:
    #     num_lst.append([int(sublst[0]), int(sublst[1])])
    # V0 = num_lst[0]
    # V1 = [num_lst[1][0]-V0[0], num_lst[1][1]-V0[1]]
    # V2 = [num_lst[2][0] - V0[0], num_lst[2][1] - V0[1]]
    if is_inside(int(digits[0]), int(digits[1]), int(digits[2]), int(digits[3]), int(digits[4]), int(digits[5]), 0, 0):
        count += 1

    # a = (det([0, 0], V2) - det(V0, V2)) / det(V1, V2)
    # b = (-1) * ((det([0, 0], V1) - det(V0, V1)) / det(V1, V2))

print(count)










