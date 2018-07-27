
def funk(n):
    count = 0
    for i in range(1, 50):
        if len(str(i**n)) == n:
            count += 1
        elif len(str(i**n)) > n:
            break
    return count


lst = []
for i in range(1,30):
    lst.append(funk(i))

print(sum(lst))



