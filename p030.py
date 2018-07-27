
numbies = []

for i in range(2,1000000):
    if sum(int(c)**5 for c in str(i)) == i:
        numbies.append(i)

print(sum(numbies))



