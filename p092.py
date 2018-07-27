

def arrives_at_89(num):
    while True:
        if num == 1:
            return False
        if num == 89:
            return True
        num = sum(int(c)**2 for c in str(num))
count = 0
for i in range(1,10000000):
    if arrives_at_89(i):
        count += 1
print count