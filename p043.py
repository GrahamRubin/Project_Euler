from itertools import permutations

primes_to_check = [1, 2, 3, 5, 7, 11, 13, 17]

def has_property(n):
    for i in range(1, 9):
        if int(str(n)[i-1:i+2]) % primes_to_check[i-1] != 0:
            # print (str(n)[i:i+3])
            # print primes_to_check[i-2]
            return False
    return True


digits_as_chars = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

pan_nums = [int(''.join(x)) for x in permutations(digits_as_chars, 10) if x[0] != '0']
sum = 0
for num in pan_nums:
    # print num
    if (has_property(num)):
        print True
        print num
        sum += num
print ("sum: " + str(sum))

# print has_property(1406357289)




