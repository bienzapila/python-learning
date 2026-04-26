n = int(input())
list0 = []
set0 = set()
for _ in range(n + 1):
    s = input()
    list0.append(s)
    set0.add(s)

if len(list0) == len(set0):
    print("OK")
else:
    print("REPEAT")
