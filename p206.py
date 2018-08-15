from itertools import permutations



# check between 1010101010 and 1389026620

def fits_forms(n, form):
    for i in range(0, len(str(form)), 2):
        if str(n)[i] != str(form)[i]:
            return False
    return True


formation = 1020304050607080900
answerrrr = 1929374254627488900
for i in range(1389026620, 1010101010, -10):
    print (i - 1010101010) // 10
    if fits_forms(i**2, formation):
        print i**2
        break



