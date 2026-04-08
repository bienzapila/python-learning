s1 = input()
s2 = input()
s1true =''
s2true =''


s1 = s1.upper()
for i in range (len(s1)):
    if s1[i].isalpha() == True:
        s1true += s1[i]

s2 = s2.upper()
for i in range (len(s2)):
    if s2[i].isalpha() == True:
        s2true += s2[i]

if s1true == s2true:
    print('YES')
else:
    print('NO')
