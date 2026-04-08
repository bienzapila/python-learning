n = int(input())
sp = []
s1 = 0 

for i in range(n):
    
    s = int(input())
    a = s + s1
    s1 = s
    if i == 0:
        continue
    sp.append(a)

print(sp)