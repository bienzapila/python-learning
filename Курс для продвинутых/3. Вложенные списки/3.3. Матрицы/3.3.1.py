n, m = int(input()), int(input())
matrix = []

a = []
cnt = 0
for i in range(n * m):
    if cnt == m:
        cnt = 0
        matrix.append(a)
        a = [input()]
        cnt += 1
    else:
        a.append(input())
        cnt += 1
    if i == n * m - 1:
        matrix.append(a)
for ma in matrix:
    print(*ma)
print()
matriz = []
for j in range(len(matrix[0])):
    for i in range(len(matrix)):
        matriz.append(matrix[i][j])

matrix = []

a = []
cnt = 0
for i in range(m * n):
    if cnt == n:
        cnt = 0
        matrix.append(a)
        a = [matriz[i]]
        cnt += 1
    else:
        a.append(matriz[i])
        cnt += 1
    if i == n * m - 1:
        matrix.append(a)

for ma in matrix:
    print(*ma)
