import math
from decimal import getcontext, Decimal


perfect_squares = [1,4,9,16,25,36,49,64,81,100]
getcontext().prec = 102

def sum_digits(irr_num):
    print irr_num
    return sum(int(c) for c in str(irr_num).replace('.', '')[0:100])


print sum(sum_digits(Decimal(x).sqrt()) for x in range(1,101) if x not in perfect_squares)




