n = int(input())
lst = []
for _ in range(n):
    lst.append(tuple(input().split()))

for l in lst:
    print(*l)
print()

for i in range(len(lst)):
    if lst[i][1] >= "4":
        print(*lst[i])
