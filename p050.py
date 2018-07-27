

def factors(n):
    return set(reduce(list.__add__, ([i, n//i] for i in range(1, int(pow(n, 0.5) + 1)) if n % i == 0)))


def primes1(n):
    """ Returns  a list of primes < n """
    sieve = [True] * (n/2)
    for i in xrange(3,int(n**0.5)+1,2):
        if sieve[i/2]:
            sieve[i*i/2::i] = [False] * ((n-i*i-1)/(2*i)+1)
    return [2] + [2*i+1 for i in xrange(1,n/2) if sieve[i]]


primes = primes1(1000000)
consecutive_primes = []
for i in range(0,len(primes)//2):
    for a in range(i, len(primes)):
        prime_sum = sum(primes[i:a+1])
        if prime_sum > 1000000:
            break
        if sum(primes[i:a+1]) in primes and a != i:
            consecutive_primes.append((a+1-i, sum(primes[i:a+1])))

print max(consecutive_primes)

