def is_pandigital(num_string):
    if len(num_string) != 9: # or str(0) in num_string:
        return False
    for i in range(1,10):
        if str(i) not in num_string:
            return False
    return True

max = 0
for i in range(1000,10000):
    num_string = str(i) + str(2*i)
    if is_pandigital(num_string) and int(num_string) > max:
        max = int(num_string)
print max



