a, b = int(input()), int(input())
for i in range (a, b+1):
    count = 0
    if i == 1:
        continue
    for j in range (1, i+1):
        if j != 1 and j != i and i % j == 0:
            count += 1
    if count == 0:
        print(i)

