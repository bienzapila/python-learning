num = list(input())
cnt = 0
for i in range(len(num) - 1, -1, -1):
    if i == 0:
        break
    cnt += 1
    if cnt % 3 == 0:
        num.insert(i, ",")

print("".join(num))
