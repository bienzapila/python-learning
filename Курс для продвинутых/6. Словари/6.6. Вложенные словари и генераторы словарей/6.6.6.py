words = ["yes", "hello"]

ans = []
for value in words:
    a = []
    for i in range(len(value)):
        a.append(ord(value[i]))
    ans.append(a)

final = {words[i]: ans[i] for i in range(len(words))}
print(final)
