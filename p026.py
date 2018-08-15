from decimal import *
from pupy.amazon_prime import is_prime
getcontext().prec = 5010



def repeated_length(n):
    n = (n*1000)%1
    for i in range(2,2500):
        # print str(n)[1:i + 1]
        # print str(n)[i + 1: 2 * i + 1]
        if str(n)[2:i+2] == str(n)[i+2:2*i + 2]:

            return i

lengths = []
for i in range(3,1000,2):
    lengths.append((repeated_length(Decimal(1)/Decimal(i)), i))

print sorted(lengths)[::-1]