

def factors(n):
    return set(reduce(list.__add__, ([i, n//i] for i in range(1, int(pow(n, 0.5) + 1)) if n % i == 0)))




num = 999
summation = sum(list(range(1,1000)))

while len(factors(summation)) < 500:
    num += 1
    summation += num
print(summation)

#
#
#
#
#
# tri_nums = [sum(list(range(1,1000)))]
# index = 0
# num = 1000
# while (len(factors(tri_nums[index])) < 500):
#     index += 1
#     tri_nums[index] = tri_nums[index-1] + num
#     num += 1
#
# print(len(factors(tri_nums[index])))





