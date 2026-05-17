numbers = [2 + 2j, 3 - 4j, 10 + 6j, -4 + 12j, 12 - 5j]
ans = 0
var = 0
for n in numbers:
    if abs(n) > ans:
        ans = abs(n)
        var = n

print(var)
print(ans)
