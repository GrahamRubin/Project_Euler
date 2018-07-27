
def reverse(n):
    return int(str(n)[::-1])


# all_nums = list(range(1000,1000000000))
all_nums = list(range(1000, 1000000))
count = 0


def all_odd_digits(n):
    for c in str(n):
        if int(c) % 2 == 0:
            return False
    return True


used_nums = []
for x in all_nums:
    rev = reverse(x)
    if len(str(x)) == len(str(rev)):
        if x not in used_nums and rev not in used_nums :
            if all_odd_digits(x+rev):
                used_nums.append(x)
                used_nums.append(rev)
                count += 2
                print(len(used_nums))


print(count+120)



