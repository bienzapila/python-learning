s = input()

for i in range(64):
    unicode = ord('А') + i
    if str(unicode) in s:
        s = s.replace(f'[u-{unicode}]', chr(unicode))

print(s)