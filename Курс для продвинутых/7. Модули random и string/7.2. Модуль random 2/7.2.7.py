import random as rnd

n, m = int(input()), int(input())
for _ in range(n):
    ans = ""
    for _ in range(m):
        k = rnd.randint(0, 2)
        if k == 0:
            ans += rnd.choice("abcdefghijkmnpqrstuvwxyz")
        elif k == 1:
            ans += rnd.choice("ABCDEFGHJKLMNPQRSTUVWXYZ")
        elif k == 2:
            ans += rnd.choice("23456789")
    flag = False
    for i in range(len(ans)):
        if ans[i].isdigit():
            flag = True
            break
    while not flag or ans == ans.lower() or ans == ans.upper():
        ans = ""
        flag = False
        for _ in range(m):
            k = rnd.randint(0, 2)
            if k == 0:
                ans += rnd.choice("abcdefghijkmnpqrstuvwxyz")
            elif k == 1:
                ans += rnd.choice("ABCDEFGHJKLMNPQRSTUVWXYZ")
            elif k == 2:
                ans += rnd.choice("23456789")
        for i in range(len(ans)):
            if ans[i].isdigit():
                flag = True
                break
    print(ans)
