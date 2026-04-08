n = int(input())
s = input()
ch = ''

for i in range(len(s)):
    decr = ord(s[i])-n
    if decr < 97:
        decr += 26
    ch += chr(decr)

print(ch)