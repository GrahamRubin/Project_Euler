


matrix = list(range(1,1001**2+1))

sum = 0
index = 0
count = 0
step = 2
sum += matrix[index]
while index < 1001**2 - 1:
    if count == 4:
        count = 0
        step += 2
    index += step
    sum += matrix[index]
    count += 1
print(sum )

