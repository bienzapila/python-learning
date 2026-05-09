s = {"write": "W", "read": "R", "execute": "X"}
n = int(input())
files = {}
for _ in range(n):
    c = input().split()
    files[c[0]] = [c[i] for i in range(1, len(c))]

operations = []
m = int(input())
for i in range(m):
    c = input().split()
    operations.append((c[1], s[c[0]]))

for i in range(len(operations)):
    if operations[i][1] in files[operations[i][0]]:
        print("OK")
    else:
        print("Access denied")
