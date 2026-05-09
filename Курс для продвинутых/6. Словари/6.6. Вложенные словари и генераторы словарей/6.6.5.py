numbers = [1, 6, 18]
ans = []
for value in numbers:
    a = []
    for i in range(1, value + 1):
        if value % i == 0:
            a.append(i)
    ans.append(sorted(a))

final = {numbers[i]: ans[i] for i in range(len(numbers))}
print(final)
