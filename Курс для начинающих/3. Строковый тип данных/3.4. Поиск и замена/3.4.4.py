a = input()
count = 0
for i in range(len(a)):
    for c in range (10):
        count += a[i].count(str(c))
print(count)