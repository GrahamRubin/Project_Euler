def primes1(n):
    """ Returns  a list of primes < n """
    sieve = [True] * (n/2)
    for i in xrange(3,int(n**0.5)+1,2):
        if sieve[i/2]:
            sieve[i*i/2::i] = [False] * ((n-i*i-1)/(2*i)+1)
    return [2] + [2*i+1 for i in xrange(1,n/2) if sieve[i]]


def is_prime(Number):
    return 2 in [Number,2**Number%Number]


def factors(n):
    return set(reduce(list.__add__, ([i, n//i] for i in range(1, int(pow(n, 0.5) + 1)) if n % i == 0)))


FatL = 600851475143
# primes = set(primes1(FatL//30))

FatL_Factors = factors(FatL)
FatL_Factors.remove(FatL)
print(len(FatL_Factors))
print(FatL_Factors)
prime_factors = []
for factor in FatL_Factors:
    if len(factors(factor))<=2:
        print(factor)
#         prime_factors.append(factor)

# print(max(prime_factors))