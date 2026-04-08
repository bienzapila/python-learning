n = int(input())
sp = []

for i in range(n):
    sp.append(input())

k = int(input())
for i in range(k):
    search = input()
    m = len(sp)

    for l in range(len(sp)):
        if search.lower() in sp[l].lower():
            sp.append(sp[l])

    sp = sp[m:]

print(*sp, sep="\n")
