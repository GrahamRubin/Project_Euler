

def num_is_palidromic(n):
    reverse = int(str(n)[::-1])
    length = len(str(n))
    return str(n)[0:length//2]==str(reverse)[0:length//2] and int(str(n)[length-1]) != 0


sum = 0
for i in range(1, 1000001):
    if (num_is_palidromic(i) and num_is_palidromic(int("{0:b}".format(i)))):
        print i
        print int("{0:b}".format(i))
        sum += i

print sum