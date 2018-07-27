# subtract one from the right most number that isn't one, and append a one to the new arrangement
def all_ones(arrangement):
    return arrangement[len(arrangement)-1] == 1

def all_ones_but_one(arrangement):
    length = len(arrangement)
    return arrangement[length - 1] > 1 and arrangement[length - 2] ==1


def arrangement_count(current_arrangement):
    count = 0
    limit = sum(current_arrangement)//2
    while not all_ones(current_arrangement):
        print current_arrangement
        count += 1
        length = len(current_arrangement)
        for i in range(0, length):
            if current_arrangement[i] > 1:
                current_arrangement[i] -= 1
                if i == 0 and current_arrangement[i] >= limit:
                    current_arrangement.insert(0, 1)
                    limit //= 2
                else:
                    current_arrangement[i-1] += 1
    return count


print(arrangement_count([1, 99]))



