m, n = int(input()), int(input())
set0 = [input() for _ in range(m)]
set1 = [input() for _ in range(n)]

for c in set1:
    print("YES") if c in set0 else print("NO")
