import math

def is_increasing(n):
    for i in range(0, len(n)-1):
        if int(n[i]) > int(n[i+1]):
            return False
    return True


def is_decreasing(n):
    for i in range(0, len(n)-1):
        if int(n[i]) < int(n[i+1]):
            return False
    return True


def is_bouncy(n):
    return not is_decreasing(str(n)) and not is_increasing(str(n))


total_count = 10
bouncy_count = 0


while int(100*bouncy_count/total_count) < 99:
    total_count += 1
    if is_bouncy(total_count):
        bouncy_count += 1
    print(total_count)
    print(bouncy_count)
    print
print(total_count)

