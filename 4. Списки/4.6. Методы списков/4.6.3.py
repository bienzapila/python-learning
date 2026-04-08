n = input().split()
for i in range(len(n)):
    n[i] = int(n[i])

mini = min(n)
maxi = max(n)

mi = n.index(mini)
ma = n.index(maxi)

n[mi] = maxi
n[ma] = mini

print(*n)
