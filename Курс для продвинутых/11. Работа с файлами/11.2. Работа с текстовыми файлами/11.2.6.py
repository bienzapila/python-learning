file = open(input())

ans = 0
for line in file:
    columns = line.split('\t')
    ans += int(columns[1]) * int(columns[2])

print(ans)
file.close()