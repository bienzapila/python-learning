n = int(input())
sp = "anton"
ind = 0


for i in range(n):
    s = input()
    ind = 0
    for k in range(len(s)):
        if s[k] == sp[ind]:
            ind += 1
        if ind == 5:
            print(i + 1, end=" ")
            break
