file = open(input())

ans = 0
for line in file:
    ans += int(line)

print(ans)

file.close()