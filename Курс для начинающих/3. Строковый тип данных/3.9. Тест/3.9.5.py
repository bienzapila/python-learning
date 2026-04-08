s = input()
res = ''

r = s.rfind('h')
l = s.find('h')

for i in range(r, l, -1):
    res += s[i]

print(f'{s[:l]}{res}{s[r:]}')
