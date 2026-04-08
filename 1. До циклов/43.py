n = int(input())
k = 2
k1 =1
k2 =1
if n ==1:
    print(1)
elif n ==2:
    print(1,1)
else:
    print(1,1, end=' ')
    for i in range(1, n-1):
        k = k1 + k2
        k2 = k1
        k1 = k
        print(k, end =' ')
