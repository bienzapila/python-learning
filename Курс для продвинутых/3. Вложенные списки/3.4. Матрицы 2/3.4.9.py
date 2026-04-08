n = int(input())
mtrx = []

for _ in range(n):
    mtrx.append(input().split())

for i in range(len(mtrx)):
    for j in range(len(mtrx[0])):
        mtrx[i][j] = int(mtrx[i][j])

lst = [a for a in range(1, n**2 + 1)]
comp = len(lst)
cnt = 0
for i in range(len(mtrx)):
    for j in range(len(mtrx[0])):
        if mtrx[i][j] in lst:
            cnt += 1
            lst.remove(mtrx[i][j])
if cnt != comp:
    print("NO")
else:

    cnt = 0
    summa = sum(mtrx[0])
    for i in range(len(mtrx)):
        if sum(mtrx[i]) == summa:
            cnt += 1
    if cnt != n:
        print("NO")
    else:

        cnt = 0
        sumc = 0
        for j in range(len(mtrx[0])):
            for i in range(len(mtrx)):
                sumc += mtrx[i][j]
            if sumc == summa:
                cnt += 1
            sumc = 0
        if cnt != n:
            print("NO")
        else:

            sumdm = 0
            for i in range(len(mtrx)):
                for j in range(len(mtrx[0])):
                    if i == j:
                        sumdm += mtrx[i][j]
            if sumdm != summa:
                print("NO")
            else:

                sumsd = 0
                j = 0
                for i in range(len(mtrx) - 1, -1, -1):
                    sumsd += mtrx[i][j]
                    j += 1
                if sumsd == summa:
                    print("YES")
                else:
                    print("NO")
