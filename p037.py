from pupy.amazon_prime import is_prime


def is_truncatable(number):
    for i in range(len(str(number))):
        if not is_prime(int(str(number)[i::])):
            return False
        if not is_prime(int(str(number)[0:len(str(number))-i])):
            return False
    return True


trunk_nums = []
for i in range(10,1000000):
    if is_truncatable(i):
        trunk_nums.append(i)

print trunk_nums
print sum(trunk_nums)





