from pupy.amazon_prime import is_prime
from pupy.amazon_prime import prime_gen
from math import sqrt






def odd_composites(limit):
    num = 9
    while num <= limit:
        if num % 2 != 0 and not is_prime(num):
            yield num
        num += 1

def rejects_conjecture(num, primes):
    for i in primes:
        if sqrt((num - i) / 2) % 1 == 0:
            return False
    return True

def extra_meth(num, primes):
    primes = [x for x in prime_gen(num, primes)]
    if rejects_conjecture(num, primes[::-1]):
        print num
    return primes


    
known_primes = None
for num in [x for x in odd_composites(10000000)][::-1]:
    known_primes = extra_meth(num, known_primes)