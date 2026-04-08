n = int(input())
for i in range(1, n*2+1, 2):
    for k in range(1, (i+1)//2+1):
        print(k, end = '')
    for m in range((i+1)//2-1, 0, -1):
        print(m, end = '')
    print()