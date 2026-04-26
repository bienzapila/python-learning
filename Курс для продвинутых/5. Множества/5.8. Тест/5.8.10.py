m, n = int(input()), int(input())
set0 = set()
for _ in range(m + n):
    s = input()
    if s in set0:
        set0.remove(s)
    else:
        set0.add(s)
print(len(set0)) if len(set0) != 0 else print("NO")
