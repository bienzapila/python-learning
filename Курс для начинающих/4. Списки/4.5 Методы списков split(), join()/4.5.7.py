s = input()
count = 0

a = s.split()

for k in range(len(a)):
    for i in range(k + 1, len(a)):
        if a[k] == a[i]:
            count += 1

print(count)
