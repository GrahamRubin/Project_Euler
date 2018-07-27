

def is_pandigital(num_string):
    if len(num_string) != 9: # or str(0) in num_string:
        return False
    for i in range(1,10):
        if str(i) not in num_string:
            return False
    return True


products = []
for i in range(1,100):
    for j in range(100, 10000):
        if is_pandigital(str(i)+str(j)+str(i*j)):
            products.append(i*j)
print 7254 in products
print sum(set(products))