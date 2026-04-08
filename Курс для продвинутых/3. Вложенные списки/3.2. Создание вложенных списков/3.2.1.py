n = int(input())

list1 = [[i for i in range(1, n + 1)] for k in range(n)]
print(*list1, sep="\n")
