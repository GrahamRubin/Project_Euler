def sum_digits(n):
    print n

    sum = 0
    while n > 0:
        sum += n % 10
        n = n//10
    print sum
    return sum



listy = []
for i in range(2, 100):
    for exp in range(1, 20):
        num = i**exp
        if i == sum_digits(num) and num > 10:
            listy.append(num)
listy.sort()
print(listy[29])

