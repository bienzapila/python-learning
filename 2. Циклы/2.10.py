n = int(input())
j = 1
for i in range (1, n + 1):
    for k in range (1, i + 1):
        print(j, end = ' ')
        j += 1
    print()