


fracs = [x*(1.0/1000000.0) for x in range(1,500000)]

reverse = fracs[::-1]
for i in range(0,len(reverse)):
    if reverse[i] <= 3.0/7:
        print reverse[i]
        print reverse[i+1]
        break