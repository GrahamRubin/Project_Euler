from itertools import permutations

digits_as_chars = [ '1', '2', '3', '4', '5', '6', '7', '8', '9']

def factors(n):
    return set(reduce(list.__add__, ([i, n//i] for i in range(1, int(pow(n, 0.5) + 1)) if n % i == 0)))

for i in range(9,0,-1):

    pan_primes = [int(''.join(x)) for x in permutations(digits_as_chars[0:i]) if int(x[i-1]) % 2 != 0 and int(x[-1]) != 5 and (x[0]) == digits_as_chars[i-1]]
    the_prime = 0
    reverse = pan_primes[::-1]
    print pan_primes[0:10]
    for i in range(0, len(reverse)):
        length = len(factors(reverse[i]))
        if length == 2:
            the_prime = reverse[i]
            break
    if the_prime != 0:
        print the_prime
        break
