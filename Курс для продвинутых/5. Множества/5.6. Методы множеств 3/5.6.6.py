s = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
s1, s2, s3 = set(input().split()), set(input().split()), set(input().split())
ans = list(s1 | s2 | s3)
for i in range(len(ans)):
    ans[i] = int(ans[i])
ans = set(ans)

print(*sorted(list(s - (ans)), key=int))
