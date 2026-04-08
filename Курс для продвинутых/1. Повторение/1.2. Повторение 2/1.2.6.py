n = int(input())
sp = []
cnt = 0

for _ in range(n):
    s = int(input())
    sp.append(s)

num = int(input())
for i in range(len(sp)):
    if cnt == 1:
        break
    for k in range(i + 1, len(sp)):
        if sp[i] * sp[k] == num:
            cnt = 1
            print("ДА")
            break
else:
    print("НЕТ")
