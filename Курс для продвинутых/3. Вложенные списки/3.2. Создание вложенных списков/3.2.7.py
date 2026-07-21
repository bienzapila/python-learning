lst = input().split()
ans = [[]]

for i in range(1, len(lst)+1):
    k = 0
    while k + i <= (len(lst)):
        ans.append([lst[n] for n in range(k, k+i)])
        k += 1

print(ans)
