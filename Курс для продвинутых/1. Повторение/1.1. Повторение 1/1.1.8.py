n, k = int(input()), int(input())
if k == 1:
    print(n)
else:
    lst = [i for i in range(1, n + 1)]

    while len(lst) >= k:
        lst = lst[k:]+(lst[:k-1])

    while len(lst) != 1:
        count = 0
        for i in range(k):
            if count > (len(lst) - 1):
                count = 0
            count += 1
        lst = lst[count:]+(lst[:count-1])

    print(lst[0])
