s = input().split()
n = int(input())


def chunk(s, n):
    ans = []

    for i in range(len(s)):
        if i == 0:
            a = [s[0]]
        elif i % n == 0:
            ans.append(a)
            a = [s[i]]
        elif i % n != 0:
            a.append(s[i])
    ans.append(a)
    return ans


print(chunk(s, n))
