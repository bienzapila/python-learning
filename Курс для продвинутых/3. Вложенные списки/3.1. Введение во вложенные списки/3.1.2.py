list1 = input()
summa = 0
cnt = 0
s = []
for l in list1:
    for a in l:
        summa += a
        cnt += 1

print(summa / cnt)
