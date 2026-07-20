n, k = int(input()), int(input())
lst = [i for i in range(1, n + 1)]

while len(lst) >= k:
    lst = lst[k:]+(lst[:k-1])
    print(lst)
print()
while len(lst) > 2:
    m = k - len(lst)
    lst += lst[:m]
    key = lst[:-1]
    if all(map(lambda x: x == key, lst)):
        print(key)
        break
    while key in lst:
        lst.remove(key)
    tlst = []
    for i in range(len(lst)):
        if lst[i] not in tlst:
            tlst.append(lst[i])
    lst = tlst
    print(f'temp {tlst}')
    print(lst)
else:
    print(lst[0])
