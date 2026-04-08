def quick_merge(n):
    for i in range(n):
        if i == 0:
            list1 = input().split()
            continue
        list2 = input().split()
        p1 = 0
        p2 = 0
        sp = []
        while p1 < len(list1) and p2 < len(list2):
            if int(list1[p1]) <= int(list2[p2]):
                sp.append(list1[p1])
                p1 += 1
            else:
                sp.append(list2[p2])
                p2 += 1
        if p1 == len(list1):
            sp.extend(list2[p2:])
        else:
            sp.extend(list1[p1:])
        list1 = sp
    print(*list1)


quick_merge(int(input()))
