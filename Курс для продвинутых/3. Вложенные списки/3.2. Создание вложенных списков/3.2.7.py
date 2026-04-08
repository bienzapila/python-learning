s = input().split()
ans = []
for i in range(len(s)):  # кол-во элементов в подсписке
    for m in range(i):  # прогоняем список
        ans.append([s[k] for k in range(m)])


ans.append(s)
print(ans)
