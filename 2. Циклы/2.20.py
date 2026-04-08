n = int(input())
if n >= 3 and n <= 19:
    for i in range (19):
        print('*', end ='')
    print('')
    for k in range(n-2):
        print('*'+' '*17+'*')
    for m in range (19):
        print('*', end ='')