n = int(input())
matr = []

for _ in range(n):
    matr.append(input().split())

for i in range(len(matr)):
    for j in range(len(matr[0])):
        matr[i][j] = int(matr[i][j])

ans = 0
for i in range(len(matr)):
    avrg = sum(matr[i]) / len(matr[i])
    ans = 0
    for j in range(len(matr[0])):
        if matr[i][j] > avrg:
            ans += 1
    print(ans)
