def primes1(n):
    """ Returns  a list of primes < n """
    sieve = [True] * (n/2)
    for i in xrange(3,int(n**0.5)+1,2):
        if sieve[i/2]:
            sieve[i*i/2::i] = [False] * ((n-i*i-1)/(2*i)+1)
    return [2] + [2*i+1 for i in xrange(1,n/2) if sieve[i]]


primes = (primes1(1000000))
circular_primes = set([3, 7])


def perms_of_prime(n):
    nums = set()
    for i in range(0, len(str(n))):
        num = int(str(n)[i:]+str(n)[0:i])
        if num not in nums:
            nums.add(num)
    print(nums)
    return nums


def perms_are_all_prime(rotated_nums):
    for p in rotated_nums:
        if p not in primes:
            # primes.remove(rotated_nums)
            return False
    for x in rotated_nums:
        primes.remove(x)
        circular_primes.add(x)
    return True



try:
    for prime in primes:
        perms_are_all_prime(perms_of_prime(prime))
except RuntimeError:
    print("whoopdee fucking doooo")

print(len(circular_primes))
print(circular_primes)