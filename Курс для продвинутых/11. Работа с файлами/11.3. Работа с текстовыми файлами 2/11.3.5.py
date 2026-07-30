with open(input()) as file:
    line = file.read()

    ans = 0
    numb = ''
    for symb in line:
        if symb.isdigit():
            numb += symb
        elif numb != '':
            ans += int(numb)
            numb = ''
    if numb != '':
        ans += int(numb)
    print(ans)
