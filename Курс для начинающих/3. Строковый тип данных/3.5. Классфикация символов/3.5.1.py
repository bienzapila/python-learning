n = int(input())
for i in range(n):
    a = input()
    if a.isspace() == True or a =='':
        print(str(i+1)+': ', 'COMMENT SHOULD BE DELETED')
    else:
        print(str(i+1)+': ', a)