s = input().split('.')
if not all(map(lambda x: x.isdigit(), s)):
    print('False')
else:
    if all(map(lambda x: True if int(x) <= 255 else False, s)):
        print('True')
    else:
        print('False')