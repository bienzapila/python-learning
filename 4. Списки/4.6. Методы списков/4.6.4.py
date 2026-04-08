n = int("".join(list(input())[1:]))

for i in range(n):
    s = input().split(" ")
    if "#" in s:
        ind = s.index("#")
        del s[ind:]
    for i in range(len(s)):
        if "#" in s[i]:
            ind = i
            del s[ind:]
            break
    s = " ".join(s)
    print(s.rtrip())
