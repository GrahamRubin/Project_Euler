

max_height = 50000

for i in range(1, max_height):
    hex = i*(2*i-1)
    for j in range(1, int(1.5*max_height)):
        pent = j*(3*j-1)//2
        if pent > hex:
            break
        elif pent == hex:
            print pent
            break




