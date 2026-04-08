a = input()
count = 0
for i in range(len(a)):
    if a[i].lower() == a[i] and a[i] in 'abcdefghijklmnopqrstuvwxyz':
        count += 1
print(count)