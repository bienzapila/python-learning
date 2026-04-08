n = int(input())
lst = []
cnt = 0

for _ in range(n):
    lst.append(input().split())

for i in range(len(lst)):
    for j in range(len(lst[0])):
        if i == j:
            cnt += int(lst[i][j])

print(cnt)
