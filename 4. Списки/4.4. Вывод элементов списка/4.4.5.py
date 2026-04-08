n = int(input())
sp =[]

for i in range(n):
    sp.append(input())

search = input()

spa =[]
for i in range(len(sp)):
    if search.upper() in sp[i].upper():
        spa.append(sp[i])

print(*spa, sep= '\n')