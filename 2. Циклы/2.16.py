n = int(input())
for h in range(24):
    for m in range(60):
        if h ** n == m:
            if h >= 10 and m >= 10:
                print(str(h)+':'+str(m))
            elif h <= 10 and m >= 10:
                print('0'+str(h)+':'+str(m))
            elif h <= 10 and m <= 10:
                print('0'+str(h)+':'+'0'+str(m))