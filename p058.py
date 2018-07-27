
def factors(n):
    return set(reduce(list.__add__, ([i, n//i] for i in range(1, int(pow(n, 0.5) + 1)) if n % i == 0)))
L = 27001
matrix = list(range(1, L**2+1))

all_nums = [1]
primes = []
# sum = 0
index = 0
count = 0
step = 2
while index < L**2 - 1:

    if count == 4:
        count = 0
        step += 2
        print((1.0 * len(primes)) / len(all_nums))
        if (index > 10 and (1.0 * len(primes)) / len(all_nums) < 0.1):
            break
    index += step
    all_nums.append(matrix[index])
    if len(factors(matrix[index])) == 2:
        primes.append(matrix[index])
    count += 1

print(step-1)
