s = input().split(" ")
sp = []
cnt = 0
for sa in s:
    if sa not in sp:
        sp.append(sa)
        cnt += 1

print(cnt)
