


def find_r_max(a, limit):
    r_max = 0
    for i in range(1, limit):
        r = ((a-1)**i+(a+1)**i)%a**2
        if  r > r_max:
            r_max = r
    return r_max
# sum = 0
# for a in range(3, 11):
#     sum += a*(a-1)
# print sum
# # print(find_r_max(7))
sum = 0
list1 = []
list2 = []
for a in range(3, 1001):
    sum += find_r_max(a, 2*a)

print(sum)