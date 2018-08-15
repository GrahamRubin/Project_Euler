

limit = 7830458
num = 1
for i in range(1, limit):
    num *= 2
    length = len(str(num))
    if length > 10:
        num = int(''.join([char for char in str(num)][length-10::]))
    # print num
print num * 28433 + 1


