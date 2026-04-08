s = input()
sp = input()

a = s.split()
for i in range(len(a)):
    print(sp.join(a[i]), end="")
    if i == len(a) - 1:
        break
    print(f"{sp} {sp}", end="")
