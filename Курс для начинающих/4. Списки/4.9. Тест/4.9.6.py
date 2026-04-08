s = input()
s.split("-")

if s[0] == "7":
    for sp in s[1:-1]:
        if len(sp) != 3 and sp.isdigit() == False:
            print("NO")
            break
    if len(s[-1]) != 4 and sp.isdigit() == False:
        print("NO")
    else:
        print("YES")
else:
    for sp in s[:-1]:
        if len(sp) != 3 and sp.isdigit() == False:
            print("NO")
            break
    if len(s[-1]) != 4 and sp.isdigit() == False:
        print("NO")
