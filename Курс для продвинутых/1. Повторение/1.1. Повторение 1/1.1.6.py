n = input()
a = n[:-5] + n[:-6:-1]
for i in range(len(a)):
    if a[i] == "0":
        continue
    else:
        k = i
        break
print(a[k:])
