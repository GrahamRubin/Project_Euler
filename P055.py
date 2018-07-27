

def is_lychrel(num):
    for i in range(50):
        num = num + int(str(num)[::-1])
        if (num == int(str(num)[::-1])):
            return False
    return True

count = 0
for i in range(10000):
    if is_lychrel(i):
        count += 1
print count
