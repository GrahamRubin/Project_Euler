


def num_triangles(p):
    count = 0
    for b in range(1, p//2):
        a = (2*b*p-p**2)/(2*(b-p))
        if a % 1:
            continue
        a = int(a)
        if a < b:
            if a**2 + b**2 == (p - a - b)**2:
                count += 1
    return count

tris = []

for i in range(3,1001):
    tris.append((num_triangles(i), i))

tris.sort()
print tris[len(tris)-1]
